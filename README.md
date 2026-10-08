# 🧬 ADN Personal — Analizador Genético Privado

<div align="center">

![Python](https://img.shields.io/badge/Python-3.9+-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.65+-red?style=for-the-badge&logo=streamlit)
![Plotly](https://img.shields.io/badge/Plotly-7.x-purple?style=for-the-badge&logo=plotly)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Privacy](https://img.shields.io/badge/Privacy-100%25%20Local-gold?style=for-the-badge)

**Explora tu ADN de MyHeritage con un dashboard interactivo y privado.**  
Análisis de más de 80 SNPs conocidos, ancestros famosos, y curiosidades genéticas — todo en tu ordenador.

[Demo](#-demo) · [Instalación](#-instalación) · [Características](#-características) · [Privacidad](#-privacidad)

</div>

---

## ✨ Características

| Sección | Descripción |
|---------|-------------|
| 🧬 **Perfil Genético** | Estadísticas de tus 600K+ SNPs con gráficas interactivas |
| 💡 **Curiosidades** | 80+ rasgos personales explicados: ojos, metabolismo, personalidad |
| 🏛️ **Ancestros Famosos** | ¿Con qué personajes históricos compartes ADN? Haplogrupos Y e mtDNA |
| 🌍 **Ancestría** | Señales de origen geográfico y % de ADN Neandertal |
| 🔬 **Explorador** | Busca cualquier SNP (rsID) en tu genoma |
| ❤️ **Salud** | Variantes de salud y metabolismo (educativo, no diagnóstico) |

## 📸 Demo

> ⚠️ Las capturas de pantalla no incluyen datos reales de ADN.

<!-- Añade capturas de pantalla aquí -->

## 🚀 Instalación

### Requisitos
- Python 3.9+
- Archivo raw DNA de **MyHeritage** (formato `.csv`)

### Pasos

```bash
# 1. Clona el repositorio
git clone https://github.com/TU_USUARIO/adn-personal.git
cd adn-personal

# 2. (Recomendado) Crea un entorno virtual
python -m venv venv

# Windows
.\venv\Scripts\Activate.ps1

# macOS/Linux
source venv/bin/activate

# 3. Instala dependencias
pip install -r requirements.txt

# 4. Ejecuta la app
python -m streamlit run app.py
```

### 🖥️ Windows (si `streamlit` no se reconoce)
```powershell
python -m streamlit run app.py
```

## 📂 Cómo añadir tu archivo de ADN

1. En **MyHeritage**: Ve a tu cuenta → **Administrar ADN** → **Descargar datos de ADN raw**
2. Descarga el archivo `.csv`
3. **Opción A**: Coloca el archivo en la carpeta del proyecto (aparece botón de carga rápida)
4. **Opción B**: Usa el uploader en el sidebar de la app

> 🔒 **El archivo nunca sale de tu ordenador**

## 📁 Estructura del proyecto

```
adn-personal/
├── app.py                    # Dashboard Streamlit principal
├── requirements.txt          # Dependencias Python
├── README.md                 # Este archivo
├── .gitignore                # Excluye datos de ADN y archivos sensibles
└── src/
    ├── __init__.py
    ├── parser.py             # Parser formato MyHeritage CSV
    ├── analyzer.py           # Clase DNAAnalyzer
    ├── snp_database.py       # Base de datos de 80+ SNPs conocidos
    └── famous_ancestors.py   # Haplogrupos y ancestros famosos
```

## 🧬 ¿Qué es un SNP?

Un **SNP** (Single Nucleotide Polymorphism) es una variación en una sola letra del código genético. Tu archivo de MyHeritage contiene ~600,000 SNPs distribuidos por todos tus cromosomas.

## 🏛️ Ancestros Famosos — ¿Cómo funciona?

El análisis de ancestros famosos usa **marcadores de haplogrupo** presentes en el chip de genotipado de MyHeritage:

- **Y-DNA**: La línea paterna de padre a hijo. Define tu "clan" de ancestros masculinos.
- **mtDNA**: La línea materna de madre a hijo/a. Define tu "clan" de ancestros femeninos.

Basándonos en investigaciones de ADN antiguo (paleo-genómica), comparamos tu haplogrupo con el de figuras históricas cuyo ADN ha sido analizado o que pertenecen con alta probabilidad al mismo linaje.

> ⚠️ Esto es una aproximación educativa. Los haplogrupos indican linajes muy distantes (miles de años), no parentesco cercano.

## 🔬 SNPs analizados

| Categoría | Nº de SNPs | Ejemplos |
|-----------|-----------|----------|
| Rasgos físicos | 15 | Color de ojos, cabello rojo, lactosa |
| Salud (educativo) | 25 | APOE, MTHFR, HFE, TCF7L2 |
| Metabolismo | 23 | Cafeína (CYP1A2), alcohol, fármacos |
| Ancestría | 8 | SLC24A5, EDAR, Duffy, Neandertal |
| Haplogrupos | 20+ | Y-DNA e mtDNA haplogroup markers |

## 🔒 Privacidad

> **Tu ADN nunca sale de tu dispositivo.**

- ✅ Todo el análisis se realiza **localmente** en tu ordenador
- ✅ La app **no envía datos** a ningún servidor
- ✅ No requiere conexión a internet para funcionar
- ✅ El `.gitignore` excluye automáticamente todos los archivos `.csv` y `.vcf`
- ✅ **Nunca subas tu archivo de ADN raw a GitHub**

## ⚠️ Aviso médico

Esta aplicación es **puramente educativa**. Los resultados:
- ❌ No son diagnósticos médicos
- ❌ No sustituyen la consulta médica
- ❌ No deben usarse para decisiones de salud

Para interpretación médica, consulta con un **genetista clínico**.

## 🛠️ Solución de problemas

### `streamlit` no se reconoce (Windows)
```powershell
python -m streamlit run app.py
```

### `ValueError: Invalid property 'titlefont'` (Plotly 7.x)
```powershell
pip install --upgrade plotly
```
Este error ocurría con la API antigua de colorbar. Ya está corregido en la versión actual.

### La app va lenta en la primera carga
Normal — carga ~600K SNPs. Tras la primera carga, los datos quedan en caché.

### Puerto 8501 ocupado
```powershell
python -m streamlit run app.py --server.port 8502
```

## 📚 Referencias científicas

- [dbSNP — Base de datos de SNPs (NCBI)](https://www.ncbi.nlm.nih.gov/snp/)
- [SNPedia](https://www.snpedia.com/) — Interpretaciones de SNPs
- [ClinVar](https://www.ncbi.nlm.nih.gov/clinvar/) — Variantes clínicas
- [Ancient DNA at Max Planck Institute](https://www.eva.mpg.de/genetics/)
- [ISOGG Y-DNA Haplogroup Tree](https://isogg.org/tree/)
- Haak et al. (2015). *Massive migration from the steppe was a source for Indo-European languages in Europe*. Nature.
- Lazaridis et al. (2022). *The genetic history of the Southern Arc*. Science.
- Margaryan et al. (2020). *Population genomics of the Viking world*. Nature.

## 📄 Licencia

MIT License — ver [LICENSE](LICENSE)

---

<div align="center">

Hecho con ❤️ y 🧬 | Los datos genéticos son fascinantes — úsalos con responsabilidad.

</div>
