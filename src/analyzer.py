"""
analyzer.py
-----------
Clase DNAAnalyzer que integra el parser y la base de datos de SNPs
para producir análisis completos del ADN del usuario.
"""

from __future__ import annotations

import logging
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd

from src.parser import parse_myheritage_csv, get_complement, get_reverse_complement
from src.snp_database import (
    SNP_DATABASE,
    get_snp_info,
    get_interpretation,
    get_all_rsids,
    get_snps_by_category,
)

logger = logging.getLogger(__name__)


class DNAAnalyzer:
    """
    Analizador completo de datos de ADN raw de MyHeritage.

    Uso básico::

        analyzer = DNAAnalyzer()
        analyzer.load_data('aldo_adn.csv')
        stats = analyzer.get_summary_stats()
        results = analyzer.analyze_all_known_snps()
    """

    def __init__(self) -> None:
        self.df: pd.DataFrame | None = None
        self._rsid_index: dict[str, dict] = {}   # rsid -> row dict
        self.filepath: str = ""

    @property
    def raw_data(self) -> pd.DataFrame | None:
        """Alias para self.df (DataFrame con los datos crudos del genoma)."""
        return self.df

    @raw_data.setter
    def raw_data(self, value: pd.DataFrame | None) -> None:
        self.df = value

    # ──────────────────────────────────────────────────────────────
    # Carga de datos
    # ──────────────────────────────────────────────────────────────

    def load_data(self, filepath_or_buffer) -> pd.DataFrame:
        """
        Carga y parsea el archivo CSV de MyHeritage.

        Parameters
        ----------
        filepath_or_buffer : str, Path, o file-like
            Archivo CSV de ADN.

        Returns
        -------
        pd.DataFrame
            DataFrame con los datos del ADN.
        """
        self.filepath = str(filepath_or_buffer) if isinstance(filepath_or_buffer, (str, Path)) else "buffer"
        self.df = parse_myheritage_csv(filepath_or_buffer)

        # Construir índice rsid -> fila para búsquedas O(1)
        self._rsid_index = {
            row['rsid']: row
            for row in self.df.to_dict('records')
        }

        logger.info(
            f"Datos cargados: {len(self.df):,} SNPs de {self.filepath}. "
            f"Índice construido con {len(self._rsid_index):,} entradas."
        )
        return self.df

    def _require_data(self) -> None:
        """Lanza ValueError si los datos no han sido cargados."""
        if self.df is None or len(self.df) == 0:
            raise ValueError("No se han cargado datos. Usa load_data() primero.")

    # ──────────────────────────────────────────────────────────────
    # Búsqueda de SNPs individuales
    # ──────────────────────────────────────────────────────────────

    def get_snp_result(self, rsid: str) -> dict[str, Any] | None:
        """
        Busca el resultado del usuario para un rsID específico.

        Intenta la orientación directa y el complemento reverso.

        Parameters
        ----------
        rsid : str
            Identificador del SNP (e.g., 'rs12913832').

        Returns
        -------
        dict | None
            Diccionario con {'rsid', 'chromosome', 'position', 'genotype',
            'allele1', 'allele2'} o None si no se encuentra.
        """
        self._require_data()
        rsid = rsid.lower().strip()
        return self._rsid_index.get(rsid)

    # ──────────────────────────────────────────────────────────────
    # Análisis de SNPs conocidos
    # ──────────────────────────────────────────────────────────────

    def analyze_all_known_snps(self) -> dict[str, dict[str, Any]]:
        """
        Analiza todos los SNPs en la base de datos contra los datos del usuario.

        Returns
        -------
        dict
            rsid -> {
                'snp_info': dict con info del SNP,
                'user_result': dict con genotipo del usuario o None,
                'interpretation': dict con interpretación o None,
                'found': bool
            }
        """
        self._require_data()
        results = {}

        for rsid, snp_info in SNP_DATABASE.items():
            user_row = self.get_snp_result(rsid)
            interp = None

            if user_row is not None:
                genotype = user_row['genotype']
                # Intentar interpretación directa
                interp = get_interpretation(rsid, genotype)

                # Si no se encuentra, intentar complemento reverso
                if interp is None and len(genotype) == 2:
                    rc = get_reverse_complement(genotype)
                    interp = get_interpretation(rsid, rc)
                    if interp is not None:
                        logger.debug(f"{rsid}: usando complemento reverso {genotype} -> {rc}")

            results[rsid] = {
                'snp_info': snp_info,
                'user_result': user_row,
                'interpretation': interp,
                'found': user_row is not None,
            }

        return results

    # ──────────────────────────────────────────────────────────────
    # Estadísticas cromosómicas
    # ──────────────────────────────────────────────────────────────

    def get_chromosome_stats(self) -> pd.DataFrame:
        """
        Retorna estadísticas por cromosoma.

        Returns
        -------
        pd.DataFrame
            Columnas: chromosome, count, heterozygous, heterozygosity_rate
        """
        self._require_data()

        # Marcar heterocigóticos
        df = self.df.copy()
        df['is_heterozygous'] = df['allele1'] != df['allele2']

        stats = (
            df.groupby('chromosome')
            .agg(
                count=('rsid', 'count'),
                heterozygous=('is_heterozygous', 'sum'),
            )
            .reset_index()
        )
        stats['heterozygosity_rate'] = (
            stats['heterozygous'] / stats['count'] * 100
        ).round(2)

        # Ordenar cromosomas: 1-22, X, Y, MT
        chrom_order = [str(i) for i in range(1, 23)] + ['X', 'Y', 'MT']
        stats['chrom_sort'] = pd.Categorical(
            stats['chromosome'], categories=chrom_order, ordered=True
        )
        stats = stats.sort_values('chrom_sort').drop(columns='chrom_sort')
        stats = stats.reset_index(drop=True)

        return stats

    # ──────────────────────────────────────────────────────────────
    # Heterocigosidad
    # ──────────────────────────────────────────────────────────────

    def get_heterozygosity_rate(self) -> float:
        """
        Calcula el porcentaje de SNPs heterocigóticos en el total del genoma.

        Returns
        -------
        float
            Porcentaje heterocigótico (0-100).
        """
        self._require_data()
        heterozygous = (self.df['allele1'] != self.df['allele2']).sum()
        return round(heterozygous / len(self.df) * 100, 2)

    # ──────────────────────────────────────────────────────────────
    # Señales de ancestría
    # ──────────────────────────────────────────────────────────────

    def get_ancestry_signals(self) -> list[dict[str, Any]]:
        """
        Analiza los SNPs marcadores de ancestría.

        Returns
        -------
        list[dict]
            Lista de dicts con info del SNP y resultado del usuario.
        """
        self._require_data()
        ancestry_snps = get_snps_by_category('Ancestría')
        signals = []

        for snp_info in ancestry_snps:
            rsid = snp_info['rsid']
            user_row = self.get_snp_result(rsid)
            interp = None

            if user_row:
                genotype = user_row['genotype']
                interp = get_interpretation(rsid, genotype)
                if interp is None and len(genotype) == 2:
                    rc = get_reverse_complement(genotype)
                    interp = get_interpretation(rsid, rc)

            signals.append({
                'snp_info': snp_info,
                'user_result': user_row,
                'interpretation': interp,
                'found': user_row is not None,
            })

        return signals

    # ──────────────────────────────────────────────────────────────
    # Curiosidades personales
    # ──────────────────────────────────────────────────────────────

    def get_curiosities(self) -> list[dict[str, Any]]:
        """
        Genera una lista de curiosidades personales basadas en los SNPs del usuario.

        Filtra solo los SNPs que se encuentran en el archivo del usuario
        y que tienen interpretación disponible.

        Returns
        -------
        list[dict]
            Lista ordenada por categoría con curiosidades interpretadas.
        """
        self._require_data()
        all_results = self.analyze_all_known_snps()
        curiosities = []

        for rsid, result in all_results.items():
            if not result['found']:
                continue
            if result['interpretation'] is None:
                continue

            curiosities.append({
                'rsid': rsid,
                'snp_info': result['snp_info'],
                'genotype': result['user_result']['genotype'],
                'interpretation': result['interpretation'],
                'category': result['snp_info'].get('category', 'Otro'),
                'subcategory': result['snp_info'].get('subcategory', ''),
                'title': result['snp_info'].get('title', rsid),
                'emoji': result['interpretation'].get('emoji', '🧬'),
                'result_text': result['interpretation'].get('result', 'N/A'),
                'detail': result['interpretation'].get('detail', ''),
                'fun_fact': result['snp_info'].get('fun_fact', ''),
                'description': result['snp_info'].get('description', ''),
                'gene': result['snp_info'].get('gene', ''),
            })

        # Ordenar: Rasgo, Metabolismo, Salud, Ancestría
        category_order = {'Rasgo': 0, 'Metabolismo': 1, 'Salud': 2, 'Ancestría': 3}
        curiosities.sort(key=lambda x: (category_order.get(x['category'], 99), x['title']))

        return curiosities

    # ──────────────────────────────────────────────────────────────
    # Estadísticas generales
    # ──────────────────────────────────────────────────────────────

    def get_summary_stats(self) -> dict[str, Any]:
        """
        Retorna estadísticas de resumen del archivo de ADN.

        Returns
        -------
        dict
            Diccionario con estadísticas clave.
        """
        self._require_data()

        total_snps = len(self.df)
        total_chromosomes = self.df['chromosome'].nunique()
        heterozygosity = self.get_heterozygosity_rate()

        # Distribución de genotipos
        genotype_counts = self.df['genotype'].value_counts()

        # SNPs en cromosomas sexuales
        sex_chroms = self.df[self.df['chromosome'].isin(['X', 'Y', 'MT'])]
        autosomal_snps = total_snps - len(sex_chroms)

        # SNPs en base de datos conocidos
        known_rsids = set(get_all_rsids())
        user_rsids = set(self.df['rsid'].tolist())
        found_known = len(known_rsids & user_rsids)

        # Cromosoma con más SNPs
        chr_counts = self.df['chromosome'].value_counts()
        top_chromosome = chr_counts.index[0] if len(chr_counts) > 0 else 'N/A'

        # Conteo por cromosoma (solo autosómicos)
        autosomal_df = self.df[~self.df['chromosome'].isin(['X', 'Y', 'MT'])]
        avg_snps_per_chr = (
            autosomal_df.groupby('chromosome').size().mean()
            if len(autosomal_df) > 0 else 0
        )

        return {
            'total_snps': total_snps,
            'total_chromosomes': total_chromosomes,
            'autosomal_snps': autosomal_snps,
            'sex_chromosome_snps': len(sex_chroms),
            'heterozygosity_rate': heterozygosity,
            'homozygosity_rate': round(100 - heterozygosity, 2),
            'top_chromosome': top_chromosome,
            'avg_snps_per_chromosome': round(avg_snps_per_chr, 0),
            'known_snps_found': found_known,
            'total_known_snps': len(known_rsids),
            'coverage_pct': round(found_known / len(known_rsids) * 100, 1) if known_rsids else 0,
        }

    # ──────────────────────────────────────────────────────────────
    # Análisis por categoría
    # ──────────────────────────────────────────────────────────────

    def get_results_by_category(self, category: str) -> list[dict[str, Any]]:
        """
        Retorna todos los resultados de una categoría específica.

        Parameters
        ----------
        category : str
            'Rasgo', 'Salud', 'Metabolismo', o 'Ancestría'
        """
        self._require_data()
        all_results = self.analyze_all_known_snps()
        return [
            r for r in all_results.values()
            if r['snp_info'].get('category') == category
        ]

    # ──────────────────────────────────────────────────────────────
    # Búsqueda libre
    # ──────────────────────────────────────────────────────────────

    def search_snp(self, query: str) -> dict[str, Any]:
        """
        Busca un SNP en el archivo del usuario y en la base de datos.

        Parameters
        ----------
        query : str
            rsID a buscar (e.g., 'rs12913832').

        Returns
        -------
        dict
            {
                'found_in_file': bool,
                'found_in_db': bool,
                'user_result': dict | None,
                'snp_info': dict | None,
                'interpretation': dict | None,
            }
        """
        self._require_data()
        rsid = query.lower().strip()

        user_row = self.get_snp_result(rsid)
        snp_info = get_snp_info(rsid)
        interp = None

        if user_row and snp_info:
            genotype = user_row['genotype']
            interp = get_interpretation(rsid, genotype)
            if interp is None and len(genotype) == 2:
                rc = get_reverse_complement(genotype)
                interp = get_interpretation(rsid, rc)

        return {
            'found_in_file': user_row is not None,
            'found_in_db': snp_info is not None,
            'user_result': user_row,
            'snp_info': snp_info,
            'interpretation': interp,
        }
