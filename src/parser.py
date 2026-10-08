"""
parser.py
---------
Módulo para parsear archivos CSV de ADN de MyHeritage.

Formato esperado:
    # Líneas de comentario al inicio
    RSID,CHROMOSOME,POSITION,RESULT
    "rs547237130","1","72526","AA"

Retorna un DataFrame con columnas:
    rsid, chromosome, position, genotype, allele1, allele2
"""

import pandas as pd
import numpy as np
import io
import logging

logger = logging.getLogger(__name__)


def _count_comment_lines(filepath_or_buffer) -> int:
    """Cuenta el número de líneas que comienzan con '#' al inicio del archivo."""
    count = 0
    if hasattr(filepath_or_buffer, 'read'):
        # Es un buffer tipo file-like
        start_pos = filepath_or_buffer.tell()
        for line in filepath_or_buffer:
            if isinstance(line, bytes):
                line = line.decode('utf-8', errors='replace')
            if line.startswith('#'):
                count += 1
            else:
                break
        filepath_or_buffer.seek(start_pos)
    else:
        with open(filepath_or_buffer, 'r', encoding='utf-8', errors='replace') as f:
            for line in f:
                if line.startswith('#'):
                    count += 1
                else:
                    break
    return count


def parse_myheritage_csv(filepath_or_buffer) -> pd.DataFrame:
    """
    Parsea un archivo CSV de MyHeritage con datos de ADN.

    Parameters
    ----------
    filepath_or_buffer : str o file-like
        Ruta al archivo CSV o buffer de bytes/texto.

    Returns
    -------
    pd.DataFrame
        DataFrame con columnas: rsid, chromosome, position, genotype, allele1, allele2
    """
    # Normalizar buffer si viene de Streamlit (bytes)
    if isinstance(filepath_or_buffer, bytes):
        filepath_or_buffer = io.BytesIO(filepath_or_buffer)

    # Para objetos file-like de Streamlit, leer todo el contenido
    if hasattr(filepath_or_buffer, 'read'):
        content = filepath_or_buffer.read()
        if isinstance(content, bytes):
            content = content.decode('utf-8', errors='replace')
        filepath_or_buffer = io.StringIO(content)

    # Contar líneas de comentario '#'
    skip_rows = _count_comment_lines(filepath_or_buffer)
    logger.info(f"Saltando {skip_rows} líneas de comentario.")

    # Leer el CSV saltando las líneas de comentario
    df = pd.read_csv(
        filepath_or_buffer,
        skiprows=skip_rows,
        dtype=str,
        na_values=['--', '??', ''],
        keep_default_na=True,
    )

    # Normalizar nombres de columnas (strip, lower, sin comillas)
    df.columns = [c.strip().strip('"').lower() for c in df.columns]

    # Renombrar columnas al esquema interno
    rename_map = {
        'rsid': 'rsid',
        'chromosome': 'chromosome',
        'position': 'position',
        'result': 'genotype',
        # Alternativas de nombres
        'chrom': 'chromosome',
        'pos': 'position',
        'genotype': 'genotype',
        'alleles': 'genotype',
    }
    df = df.rename(columns={k: v for k, v in rename_map.items() if k in df.columns})

    # Verificar columnas mínimas requeridas
    required = {'rsid', 'chromosome', 'position', 'genotype'}
    missing = required - set(df.columns)
    if missing:
        raise ValueError(
            f"El archivo CSV no contiene las columnas requeridas: {missing}. "
            f"Columnas encontradas: {list(df.columns)}"
        )

    # Limpiar valores: quitar comillas residuales y espacios
    for col in df.columns:
        df[col] = df[col].astype(str).str.strip().str.strip('"').str.strip()

    # Reemplazar 'nan' string por NaN real
    df.replace('nan', np.nan, inplace=True)

    # Normalizar rsid: minúsculas y sin espacios
    df['rsid'] = df['rsid'].str.lower().str.strip()

    # Normalizar cromosoma: mayúsculas (X, Y, MT)
    df['chromosome'] = df['chromosome'].str.upper().str.strip()

    # Normalizar position a int (ignorar no numéricos)
    df['position'] = pd.to_numeric(df['position'], errors='coerce').astype('Int64')

    # Normalizar genotype: mayúsculas, sin espacios
    df['genotype'] = df['genotype'].str.upper().str.strip()

    # Eliminar filas sin rsid o genotype válidos
    df = df.dropna(subset=['rsid', 'genotype'])
    df = df[df['rsid'].str.startswith('rs')]

    # Extraer allele1 y allele2
    df['allele1'] = df['genotype'].str[0]
    df['allele2'] = df['genotype'].str[1] if df['genotype'].str.len().max() >= 2 else df['allele1']

    # Corregir allele2 para genotipos de 1 carácter (hemizigóticos, Y, MT)
    mask_single = df['genotype'].str.len() == 1
    df.loc[mask_single, 'allele2'] = df.loc[mask_single, 'allele1']

    # Reset index
    df = df.reset_index(drop=True)

    logger.info(
        f"Archivo parseado correctamente: {len(df):,} SNPs, "
        f"{df['chromosome'].nunique()} cromosomas."
    )

    return df[['rsid', 'chromosome', 'position', 'genotype', 'allele1', 'allele2']]


def get_complement(nucleotide: str) -> str:
    """Retorna el complemento de un nucleótido."""
    comp = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join(comp.get(n, n) for n in nucleotide.upper())


def get_reverse_complement(genotype: str) -> str:
    """Retorna el complemento reverso de un genotipo de 2 alelos."""
    if len(genotype) < 2:
        return get_complement(genotype)
    return get_complement(genotype[1]) + get_complement(genotype[0])
