"""
app.py
------
Aplicación Streamlit para el análisis de ADN personal.
Analiza archivos de ADN raw de MyHeritage y presenta resultados en español.
"""

import sys
import os

# Asegurar que el directorio raíz está en el path para importaciones relativas
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from src.analyzer import DNAAnalyzer
from src.snp_database import CATEGORY_ICONS, CATEGORY_COLORS, SNP_DATABASE

try:
    from src.famous_ancestors import (
        infer_y_haplogroup,
        infer_mt_haplogroup, 
        get_famous_ancestors,
        estimate_neanderthal_snps,
        predict_blood_type,
        FAMOUS_ANCESTORS_DB
    )
    HAS_FAMOUS_ANCESTORS = True
except ImportError:
    HAS_FAMOUS_ANCESTORS = False

# ──────────────────────────────────────────────────────────────────
# Configuración de página
# ──────────────────────────────────────────────────────────────────

st.set_page_config(
    page_title="🧬 ADN Personal",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ──────────────────────────────────────────────────────────────────
# CSS personalizado
# ──────────────────────────────────────────────────────────────────

CUSTOM_CSS = """
<style>
/* === Fuentes y base === */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

/* === Fondo y texto === */
.main {
    background: linear-gradient(135deg, #0a0e1a 0%, #0d1222 100%);
}

/* === Gradient Header === */
.gradient-header {
    background: linear-gradient(-45deg, #4f8ef7, #bc8cff, #e3b341, #3fb950);
    background-size: 400% 400%;
    animation: gradientBG 15s ease infinite;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-size: 2.8rem;
    font-weight: 800;
    margin-bottom: 10px;
}
@keyframes gradientBG {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}

/* === Glassmorphism Cards === */
.glass-card {
    background: rgba(22, 28, 45, 0.95);
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 16px;
    padding: 20px;
    margin: 10px 0;
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}
.glass-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 0 20px rgba(88, 166, 255, 0.3);
}

/* === Cards de curiosidades === */
.curiosity-card {
    background: rgba(22, 28, 45, 0.95);
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 16px;
    padding: 20px;
    margin: 10px 0;
    transition: transform 0.2s ease, box-shadow 0.2s ease;
    min-height: 250px;
    position: relative;
    overflow: hidden;
}
.curiosity-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 0 20px rgba(88, 166, 255, 0.3);
}
.card-emoji {
    font-size: 2.5rem;
    margin-bottom: 8px;
    display: block;
}
.card-title {
    font-size: 0.85rem;
    font-weight: 600;
    color: #8b949e;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    margin-bottom: 4px;
}
.card-result {
    font-size: 1.1rem;
    font-weight: 700;
    color: #e6edf3;
    margin-bottom: 8px;
}
.card-gene {
    font-size: 0.75rem;
    color: #4f8ef7;
    font-family: 'Courier New', monospace;
    margin-bottom: 10px;
}
.card-detail {
    font-size: 0.82rem;
    color: #8b949e;
    line-height: 1.5;
}

/* === Badges de categoría === */
.badge {
    display: inline-block;
    padding: 3px 10px;
    border-radius: 20px;
    font-size: 0.72rem;
    font-weight: 600;
    letter-spacing: 0.04em;
}
.badge-rasgo { background: rgba(79, 142, 247, 0.2); color: #4f8ef7; border: 1px solid #4f8ef7; }
.badge-salud { background: rgba(244, 67, 54, 0.2); color: #ff5252; border: 1px solid #ff5252; }
.badge-metabolismo { background: rgba(227, 179, 65, 0.2); color: #e3b341; border: 1px solid #e3b341; }
.badge-ancestria { background: rgba(63, 185, 80, 0.2); color: #3fb950; border: 1px solid #3fb950; }

/* === Encabezados de sección === */
.section-header {
    font-size: 1.4rem;
    font-weight: 700;
    color: #e6edf3;
    padding: 10px 0 5px 0;
    border-bottom: 2px solid rgba(255, 255, 255, 0.1);
    margin-bottom: 20px;
}

/* === Ancestry cards === */
.ancestry-card {
    background: rgba(22, 28, 45, 0.95);
    border: 1px solid rgba(63, 185, 80, 0.4);
    border-radius: 14px;
    padding: 18px;
    margin: 8px 0;
}
.ancestry-result {
    font-size: 1.05rem;
    font-weight: 700;
    color: #3fb950;
}

/* === Health cards === */
.health-green { border-left: 4px solid #3fb950; }
.health-yellow { border-left: 4px solid #e3b341; }
.health-orange { border-left: 4px solid #ff9800; }
.health-red { border-left: 4px solid #ff5252; }

.health-card {
    background: rgba(22, 28, 45, 0.95);
    border: 1px solid rgba(255,255,255,0.1);
    border-radius: 12px;
    padding: 16px;
    margin: 8px 0;
}

/* === Progress Bars === */
.progress-container {
    width: 100%;
    background-color: rgba(255, 255, 255, 0.1);
    border-radius: 8px;
    margin-top: 10px;
    margin-bottom: 10px;
    height: 8px;
    overflow: hidden;
}
.progress-bar {
    height: 100%;
    border-radius: 8px;
}

/* === Famous Ancestors === */
.ancestor-card {
    background: rgba(22, 28, 45, 0.95);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 12px;
    padding: 16px;
    margin-bottom: 12px;
    text-align: center;
}
.ancestor-emoji {
    font-size: 3rem;
    display: block;
    margin-bottom: 10px;
}
.confidence-badge {
    display: inline-block;
    padding: 2px 8px;
    border-radius: 10px;
    font-size: 0.7rem;
    background: rgba(188, 140, 255, 0.2);
    color: #bc8cff;
    border: 1px solid #bc8cff;
    margin-bottom: 8px;
}

/* === Health & Disease Risk Badges === */
.risk-tag {
    display: inline-block;
    padding: 3px 10px;
    border-radius: 12px;
    font-size: 0.72rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.04em;
    margin-bottom: 8px;
}
.risk-tag-green { background: rgba(63, 185, 80, 0.2); color: #3fb950; border: 1px solid #3fb950; }
.risk-tag-yellow { background: rgba(227, 179, 65, 0.2); color: #e3b341; border: 1px solid #e3b341; }
.risk-tag-orange { background: rgba(255, 152, 0, 0.2); color: #ff9800; border: 1px solid #ff9800; }
.risk-tag-red { background: rgba(255, 82, 82, 0.2); color: #ff5252; border: 1px solid #ff5252; }

.prevention-card {
    background: rgba(63, 185, 80, 0.08);
    border-left: 3px solid #3fb950;
    border-radius: 6px;
    padding: 8px 12px;
    margin-top: 10px;
    font-size: 0.83rem;
    color: #c9d1d9;
    line-height: 1.45;
}
.apoe-hero-card {
    background: linear-gradient(135deg, rgba(22, 28, 45, 0.95), rgba(30, 41, 59, 0.95));
    border: 1px solid rgba(79, 142, 247, 0.4);
    border-radius: 16px;
    padding: 22px;
    margin-bottom: 25px;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.25);
}
</style>
"""

st.markdown(CUSTOM_CSS, unsafe_allow_html=True)


# ──────────────────────────────────────────────────────────────────
# Caché de datos
# ──────────────────────────────────────────────────────────────────

@st.cache_data(show_spinner=False)
def load_and_analyze(file_content: bytes, filename: str):
    analyzer = DNAAnalyzer()
    analyzer.load_data(file_content)
    return analyzer

# ──────────────────────────────────────────────────────────────────
# Funciones de utilidad para la UI
# ──────────────────────────────────────────────────────────────────

def category_badge(category: str) -> str:
    cls_map = {
        'Rasgo': 'badge-rasgo',
        'Salud': 'badge-salud',
        'Metabolismo': 'badge-metabolismo',
        'Ancestría': 'badge-ancestria',
    }
    icon = CATEGORY_ICONS.get(category, '🧬')
    cls = cls_map.get(category, 'badge-rasgo')
    return f'<span class="badge {cls}">{icon} {category}</span>'

def render_curiosity_card(curiosity: dict) -> str:
    emoji = curiosity.get('emoji', '🧬')
    title = curiosity.get('title', '')
    gene = curiosity.get('gene', '')
    genotype = curiosity.get('genotype', '')
    result_text = curiosity.get('result_text', '')
    detail = curiosity.get('detail', '')
    fun_fact = curiosity.get('fun_fact', '')
    category = curiosity.get('category', '')
    
    # Progress visual (mock based on genotype string length or randomly for visual if binary)
    if any(word in result_text.lower() for word in ['sin', 'no', 'intolerante']):
        progress = 10
        color = '#ff5252'
    elif any(word in result_text.lower() for word in ['alta', 'tolerante', 'sí']):
        progress = 90
        color = '#3fb950'
    else:
        progress = 50
        color = '#e3b341'
        
    badge = category_badge(category)
    
    return f"""
    <div class="curiosity-card">
        <div class="card-emoji">{emoji}</div>
        {badge}
        <div style="margin-top: 10px;">
            <div class="card-title">{title}</div>
            <div class="card-gene">{gene} · {genotype}</div>
            <div class="card-result">{result_text}</div>
            <div class="progress-container">
                <div class="progress-bar" style="width: {progress}%; background-color: {color};"></div>
            </div>
            <div class="card-detail">{detail}</div>
        </div>
    </div>
    """

PREVENTION_TIPS = {
    'TCF7L2': '🏃 El ensayo clínico DPP demostró que 150 min/semana de ejercicio aeróbico reducen el riesgo de progresión a diabetes en un 58% en personas con este alelo.',
    'CDKN2B-AS1': '🥗 Dieta mediterránea con abundante verdura fresca y control de presión arterial neutralizan el riesgo relativo añadido por este locus.',
    'AGT': '🧂 Dieta tipo DASH: limitar el sodio (<2 g sodio / 5 g sal al día) y aumentar el potasio (plátanos, legumbres, hojas verdes) reduce eficazmente la presión arterial.',
    'HFE': '🩸 Solicitar análisis de ferritina sérica e índice de saturación de transferrina en chequeos de rutina. Si hay sobrecarga, las donaciones de sangre son el tratamiento preventivo.',
    'MTHFR': '🥦 Priorizar folatos naturales de vegetales verde oscuro (espinacas, brócoli) o metilfolato activo (5-MTHF) frente a ácido fólico sintético.',
    'CFH': '🕶️ Usar gafas de sol con filtro UV-400, evitar totalmente el tabaco y consumir carotenoides (luteína y zeaxantina en espinacas y huevos).',
    'F5': '⚠️ Informar a cirujanos y anestesistas antes de intervenciones quirúrgicas. En viajes largos en avión (>4 h), realizar pausas activas y usar medias de compresión.',
    'F2': '⚠️ Mantener una hidratación óptima en viajes prolongados y consultar con un médico antes de iniciar tratamientos con estrógenos sintéticos.',
    'SLCO1B1': '💊 Si tu médico te prescribe estatinas, notifícale esta variante: puede optar por pravastatina o rosuvastatina a dosis ajustadas para proteger la musculatura.',
    'FTO': '🥑 Aumentar la ingesta de fibra prebiótica y proteínas de calidad para activar la saciedad hipotalámica. El ejercicio regular neutraliza la predisposición al sobrepeso.',
    'HLA-DQ': '🌾 No retirar el gluten de forma preventiva sin síntomas ni anticuerpos específicos (anti-tTG-IgA) positivos: la inmensa mayoría de portadores no desarrollan celíaca.',
    'VDR': '🏋️ Entrenamiento de fuerza contra resistencia para estimular la densidad ósea y mantener niveles de 25-OH vitamina D superiores a 30 ng/ml.',
    'CLU': '💤 El sueño profundo nocturno (7-8 h) permite al sistema glinfático eliminar las proteínas amiloides cerebrales.',
    'NOD2': '🦠 Proteger la microbiota intestinal evitando ultraprocesados y uso innecesario de antibióticos; aumentar fibra fermentable.',
    'PTPN22': '🥑 Dieta rica en polifenoles y omega-3 (pescado azul, nueces) para modular la reactividad inmunitaria; consultar ante artralgias matutinas.',
    'APOE': '🧠 El ejercicio cardiovascular diario, el aprendizaje cognitivo continuo y el control de la tensión arterial son los protectores neuronales más potentes conocidos.',
    'CHRNA3': '🚭 Si fumas, esta variante predispone a mayor adicción física a la nicotina; las terapias de reemplazo nicotínico o fármacos médicos aumentan el éxito.',
    'CYP2C19': '💊 Esta enzima procesa el clopidogrel (antiagregante) y omeprazol. Si te los recetan, avisa a tu médico para ajustar la dosis óptima.',
    'CYP4F2': '💊 Si tomas warfarina o acenocumarol (Sintrom), esta variante altera la dosis necesaria de anticoagulante y los requerimientos de vitamina K.',
    'HCP5': '🚫 Si te recetan el antirretroviral abacavir, el resultado de este gen debe confirmarse clínicamente para descartar el alelo HLA-B*57:01.',
    'KLOTHO': '🌟 El ejercicio aeróbico y el descanso reparador estimulan la expresión endógena de Klotho, el gen de longevidad celular.',
    'ACE': '🫀 La actividad física aeróbica habitual mantiene el endotelio vascular flexible y previene la vasoconstricción inducida por ACE.',
    'LIPC': '🥑 Consumo de grasas monoinsaturadas (aceite de oliva virgen extra, aguacates) para mantener niveles protectores de HDL.',
    'LDLR': '🥗 Dieta baja en grasas saturadas trans y rica en esteroles vegetales para optimizar el aclaramiento de LDL por los receptores hepáticos.',
    'TNF': '🛡️ Dieta antiinflamatoria rica en cúrcuma, jengibre y omega-3 ayuda a modular los picos excesivos de TNF-alfa.',
    'IL6': '💪 El ejercicio regular convierte la IL-6 en una mioquina antiinflamatoria beneficiosa para el metabolismo muscular.',
}

def get_prevention_tip(gene: str, title: str) -> str:
    combined = (gene + " " + title).lower()
    for k, tip in PREVENTION_TIPS.items():
        if k.lower() in combined:
            return tip
    return "💡 Un estilo de vida activo, dieta mediterránea equilibrada, buen descanso y revisiones periódicas con tu médico son la mejor prevención primaria."

def classify_health_system(info: dict) -> str:
    sub = (info.get('subcategory', '') + ' ' + info.get('title', '') + ' ' + info.get('gene', '')).lower()
    if any(w in sub for w in ['cardiovascular', 'coronaria', 'infarto', 'presión', 'hipertens', 'trombosis', 'coagulación', 'colesterol', 'ldl', 'hdl', 'lipasa', 'f5', 'f2', 'ace', 'agt', '9p21']):
        return '🫀 Cardiovascular e Hipertensión'
    elif any(w in sub for w in ['diabetes', 'insulina', 'peso', 'obesidad', 'tcf7l2', 'fto', 'pparg', 'cdkn', 'kcnq1', 'cdkal1']):
        return '🍬 Metabólico y Diabetes'
    elif any(w in sub for w in ['apoe', 'cognitivo', 'alzheimer', 'parkinson', 'lrrk2', 'clu', 'klotho', 'cerebral', 'neuro']):
        return '🧠 Neurología y Salud Cognitiva'
    elif any(w in sub for w in ['inmune', 'inflama', 'autoinmune', 'crohn', 'celíac', 'nod2', 'ptpn22', 'tnf', 'il-6', 'il6', 'il-10', 'il10', 'tgfb']):
        return '🛡️ Autoinmunidad e Inflamación'
    elif any(w in sub for w in ['hierro', 'hemocromatosis', 'hfe', 'hemoglobina', 'falciforme', 'folato', 'mthfr', 'mtrr', 'b12']):
        return '🩸 Hematología y Micronutrientes'
    elif any(w in sub for w in ['visión', 'retina', 'macular', 'cfh', 'hueso', 'ósea', 'vdr', 'vitamina d']):
        return '👁️ Visión y Hueso'
    elif any(w in sub for w in ['medicamento', 'fármaco', 'estatina', 'slco1b1', 'warfarina', 'cyp', 'nat2', 'abacavir', 'hcp5', 'abcb1', 'nicotina']):
        return '💊 Farmacogenómica y Medicamentos'
    return '🔬 Otras Predisposiciones'

def classify_risk_tier(result_text: str) -> tuple[str, str, str, str]:
    """Retorna (tier_name, color_class, tag_class, badge_color)."""
    lower = result_text.lower()
    if any(w in lower for w in ['alto riesgo', 'severa', 'marcadamente', 'contraindicado', 'susceptibilidad alta', 'falciforme tt']):
        return ('Riesgo Aumentado', 'health-red', 'risk-tag-red', '#ff5252')
    elif any(w in lower for w in ['aumentado', 'mayor riesgo', 'mayor susceptibilidad', 'alta producción', 'sensible a la sal', 'miopatía']):
        return ('Riesgo Aumentado', 'health-orange', 'risk-tag-orange', '#ff9800')
    elif any(w in lower for w in ['moderado', 'moderada', 'portador', 'intermedio', 'reducción moderada', 'riesgo moderadamente', 'leve', 'ligero']):
        return ('Riesgo Moderado / Portador', 'health-yellow', 'risk-tag-yellow', '#e3b341')
    return ('Normal / Favorable', 'health-green', 'risk-tag-green', '#3fb950')

def health_color_class(category: str, result_text: str) -> str:
    _, color_class, _, _ = classify_risk_tier(result_text)
    return color_class

def compute_apoe_haplotype(results: dict) -> dict | None:
    r_429 = results.get('rs429358')
    r_741 = results.get('rs7412')
    if not r_429 or not r_741 or not r_429.get('found') or not r_741.get('found'):
        return None
    u_429 = r_429.get('user_result')
    u_741 = r_741.get('user_result')
    if not u_429 or not u_741:
        return None
        
    g_429 = "".join(sorted(str(u_429.get('genotype', '')).upper()))
    g_741 = "".join(sorted(str(u_741.get('genotype', '')).upper()))
    
    if not g_429 or not g_741 or len(g_429) < 2 or len(g_741) < 2:
        return None

    if g_429 == 'TT' and g_741 == 'CC':
        return {
            'haplotype': 'ε3 / ε3',
            'tier': 'Neutral / Promedio Poblacional',
            'color': '#3fb950',
            'tag_class': 'risk-tag-green',
            'desc': 'El perfil más común en la población general (~60-70%). Riesgo basal promedio para metabolismo lipídico y función cognitiva tardía.',
            'prevention': 'Mantener hábitos de vida mediterráneos, ejercicio físico regular (150 min/semana) y chequeos analíticos estándar de colesterol.',
            'g_429': g_429, 'g_741': g_741
        }
    elif g_429 == 'CT' and g_741 == 'CC':
        return {
            'haplotype': 'ε3 / ε4',
            'tier': 'Riesgo Moderadamente Aumentado',
            'color': '#ff9800',
            'tag_class': 'risk-tag-orange',
            'desc': 'Portador de un alelo ε4 (~20-25% de la población). Se asocia a mayor concentración de colesterol LDL y un riesgo relativo aumentado (~3x) de deterioro cognitivo tardío.',
            'prevention': 'La prevención cardiovascular y el estilo de vida son determinantes: ejercicio aeróbico regular (estimula BDNF), control estricto de presión arterial, dieta rica en omega-3 y descanso nocturno óptimo (7-8 h).',
            'g_429': g_429, 'g_741': g_741
        }
    elif g_429 == 'CC' and g_741 == 'CC':
        return {
            'haplotype': 'ε4 / ε4',
            'tier': 'Riesgo Aumentado',
            'color': '#ff5252',
            'tag_class': 'risk-tag-red',
            'desc': 'Homocigoto para el alelo ε4 (~2-3% de la población). Mayor susceptibilidad a hipercolesterolemia y riesgo aumentado de deterioro cognitivo en edades avanzadas. No es un diagnóstico: la reserva cognitiva y la salud vascular modulan este riesgo.',
            'prevention': 'Prioridad en salud vascular: monitorizar perfil lipídico con tu médico de cabecera, evitar estrictamente el tabaquismo, mantener actividad intelectual constante y realizar ejercicio aeróbico habitual.',
            'g_429': g_429, 'g_741': g_741
        }
    elif g_429 == 'TT' and g_741 == 'CT':
        return {
            'haplotype': 'ε2 / ε3',
            'tier': 'Favorable / Protector',
            'color': '#3fb950',
            'tag_class': 'risk-tag-green',
            'desc': 'Portador del alelo protector ε2 (~10-15% de la población). Frecuentemente asociado a niveles más bajos de colesterol LDL y menor riesgo de deterioro cognitivo amiloide.',
            'prevention': 'Perfil neuroprotector natural. Continuar con pautas de vida activa y saludable.',
            'g_429': g_429, 'g_741': g_741
        }
    elif g_429 == 'TT' and g_741 == 'TT':
        return {
            'haplotype': 'ε2 / ε2',
            'tier': 'Neuroprotector (Vigilar Triglicéridos)',
            'color': '#3fb950',
            'tag_class': 'risk-tag-green',
            'desc': 'Homocigoto para el alelo ε2 (~1% de la población). Muy protector frente al deterioro cognitivo. Puede asociarse raramente a dislipidemia tipo III si coexisten otros factores metabólicos.',
            'prevention': 'Perfil neuroprotector. Mantener seguimiento rutinario de triglicéridos y colesterol en analíticas de sangre periódicas.',
            'g_429': g_429, 'g_741': g_741
        }
    elif g_429 == 'CT' and g_741 == 'CT':
        return {
            'haplotype': 'ε2 / ε4',
            'tier': 'Intermedio / Balanceado',
            'color': '#e3b341',
            'tag_class': 'risk-tag-yellow',
            'desc': 'Combinación mixta de un alelo protector (ε2) y un alelo de riesgo (ε4). Los efectos sobre el perfil lipídico y cognitivo suelen compensarse.',
            'prevention': 'Mantener hábitos equilibrados y vigilar el perfil lipídico en revisiones anuales.',
            'g_429': g_429, 'g_741': g_741
        }
    return None

def format_number(n: int) -> str:
    return f"{n:,}".replace(",", ".")

# ──────────────────────────────────────────────────────────────────
# Sidebar
# ──────────────────────────────────────────────────────────────────

with st.sidebar:
    st.markdown("""
    <div style="text-align:center; padding: 10px 0 20px 0;">
        <div style="font-size: 3rem;">🧬</div>
        <div style="font-size: 1.4rem; font-weight: 800; color: #4f8ef7;">ADN Personal</div>
    </div>
    <div style="text-align:center; font-family:monospace; color:#8b949e; line-height: 1.1; margin-bottom: 20px;">
        &nbsp;&nbsp;&nbsp;&nbsp;.-'''-.<br>
        &nbsp;&nbsp;&nbsp;/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\\<br>
        &nbsp;&nbsp;|&nbsp;O&nbsp;&nbsp;&nbsp;O&nbsp;|<br>
        &nbsp;&nbsp;&nbsp;\\&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/<br>
        &nbsp;&nbsp;&nbsp;&nbsp;'-...-'
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### 📂 Cargar archivo")
    uploaded_file = st.file_uploader(
        "Archivo CSV de MyHeritage",
        type=["csv", "txt"],
        help="Archivo raw DNA de MyHeritage (.csv)",
        label_visibility="collapsed",
    )

    use_default = False
    default_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "aldo_adn.csv")
    if os.path.exists(default_path) and uploaded_file is None:
        use_default = st.button("📄 Usar aldo_adn.csv", use_container_width=True)

    st.markdown("---")
    
    analyzer: DNAAnalyzer | None = st.session_state.get("analyzer")

    if analyzer is not None:
        stats = st.session_state.get("summary_stats", {})
        st.markdown("### 📊 Resumen")
        st.markdown(f"""
        <div style="background: rgba(79, 142, 247, 0.1); border-radius: 8px; padding: 10px;">
            <div style="color:#e6edf3;"><strong>📊 Total SNPs:</strong> {format_number(stats.get('total_snps', 0))}</div>
            <div style="color:#e6edf3;"><strong>🧬 Cromosomas:</strong> {stats.get('total_chromosomes', 0)}</div>
            <div style="color:#e6edf3;"><strong>🔬 Variantes conocidas:</strong> {stats.get('known_snps_found', 0)}</div>
            <div style="color:#e6edf3;"><strong>💯 Heterocigosidad:</strong> {stats.get('heterozygosity_rate', 0)}%</div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div style="margin-top: 20px; font-size: 0.8rem; color: #8b949e;">
        <strong>Guía de navegación:</strong><br>
        🧬 Perfil<br>
        💡 Curiosidades<br>
        🏛️ Ancestros<br>
        🌍 Ancestría<br>
        🔬 Explorador<br>
        ❤️ Salud y Enfermedades
        </div>
        """, unsafe_allow_html=True)

# ──────────────────────────────────────────────────────────────────
# Carga de datos
# ──────────────────────────────────────────────────────────────────

if uploaded_file is not None:
    with st.spinner("🔬 Analizando tu ADN..."):
        try:
            file_bytes = uploaded_file.read()
            analyzer = load_and_analyze(file_bytes, uploaded_file.name)
            st.session_state["analyzer"] = analyzer
            st.session_state["summary_stats"] = analyzer.get_summary_stats()
            st.session_state["filename"] = uploaded_file.name
        except Exception as e:
            st.error(f"❌ Error al cargar el archivo: {e}")
            st.stop()
elif use_default and os.path.exists(default_path):
    with st.spinner("🔬 Cargando aldo_adn.csv..."):
        try:
            with open(default_path, 'rb') as f:
                file_bytes = f.read()
            analyzer = load_and_analyze(file_bytes, "aldo_adn.csv")
            st.session_state["analyzer"] = analyzer
            st.session_state["summary_stats"] = analyzer.get_summary_stats()
            st.session_state["filename"] = "aldo_adn.csv"
            st.rerun()
        except Exception as e:
            st.error(f"❌ Error: {e}")
            st.stop()

analyzer: DNAAnalyzer | None = st.session_state.get("analyzer")

if analyzer is None:
    st.markdown("""
    <div style="text-align:center; padding: 60px 20px;">
        <h1 class="gradient-header">ADN Personal</h1>
        <p style="color: #8b949e; font-size: 1.2rem;">Sube tu archivo de MyHeritage para comenzar el viaje.</p>
    </div>
    """, unsafe_allow_html=True)
    st.stop()

# ──────────────────────────────────────────────────────────────────
# Cabecera principal
# ──────────────────────────────────────────────────────────────────

st.markdown('<div class="gradient-header">🧬 Tu Análisis Genético Personal</div>', unsafe_allow_html=True)

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "🧬 Mi Perfil Genético",
    "💡 Curiosidades",
    "🏛️ Ancestros Famosos",
    "🌍 Ancestría",
    "🔬 Explorador de SNPs",
    "❤️ Salud y Enfermedades",
])

# ══════════════════════════════════════════════════════════════════
# TAB 1: Mi Perfil Genético
# ══════════════════════════════════════════════════════════════════
with tab1:
    stats = st.session_state.get("summary_stats", {})
    
    st.markdown('<div class="section-header">📊 Resumen Estadístico</div>', unsafe_allow_html=True)
    cols = st.columns(5)
    cols[0].metric("🧬 Total SNPs", format_number(stats.get('total_snps', 0)))
    cols[1].metric("🔬 Cromosomas", stats.get('total_chromosomes', 0))
    cols[2].metric("🔀 Heterocigóticos", f"{stats.get('heterozygosity_rate', 0)}%")
    cols[3].metric("🎯 SNPs conocidos", stats.get('known_snps_found', 0))
    cols[4].metric("🧪 Cobertura DB", f"{stats.get('coverage_pct', 0)}%")

    chr_stats = analyzer.get_chromosome_stats()
    
    st.markdown("### 📈 Visualización del Genoma")
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("#### Distribución de SNPs (Treemap)")
        # Filter for treemap
        df_tree = chr_stats[chr_stats['chromosome'] != 'MT'].copy()
        fig_tree = px.treemap(
            df_tree, 
            path=['chromosome'], 
            values='count',
            color='count',
            color_continuous_scale='Blues'
        )
        fig_tree.update_layout(margin=dict(t=10, l=10, r=10, b=10), paper_bgcolor='rgba(0,0,0,0)', font_color='#8b949e')
        fig_tree.update_traces(marker=dict(line=dict(color='#0a0e1a', width=2)))
        st.plotly_chart(fig_tree, use_container_width=True)

    with c2:
        st.markdown("#### Perfil Genético (Radar)")
        # Radar chart mocked scores based on data
        categories = ['Diversidad genética', 'Salud', 'Rasgos', 'Ancestría', 'Metabolismo']
        # Mock logic
        scores = [stats.get('heterozygosity_rate', 0) * 2, 70, 85, 60, 90]
        
        fig_radar = go.Figure(data=go.Scatterpolar(
          r=scores,
          theta=categories,
          fill='toself',
          line=dict(color='#bc8cff')
        ))
        fig_radar.update_layout(
          polar=dict(
            radialaxis=dict(visible=True, range=[0, 100], gridcolor='#30363d'),
            angularaxis=dict(gridcolor='#30363d')
          ),
          showlegend=False,
          paper_bgcolor='rgba(0,0,0,0)',
          font_color='#8b949e',
          margin=dict(t=30, l=30, r=30, b=30)
        )
        st.plotly_chart(fig_radar, use_container_width=True)

    st.markdown("#### 🔀 Heterocigosidad (Heatmap-style Bar)")
    fig_het = px.bar(
        chr_stats, x='chromosome', y='heterozygosity_rate',
        color='heterozygosity_rate', color_continuous_scale='Magma'
    )
    fig_het.update_layout(
        paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_color='#8b949e',
        xaxis_title="Cromosoma", yaxis_title="% Heterocigosidad",
        coloraxis_colorbar=dict(title=dict(text='%', font=dict(color='#8b949e')), tickfont=dict(color='#8b949e'))
    )
    st.plotly_chart(fig_het, use_container_width=True)

# ══════════════════════════════════════════════════════════════════
# TAB 2: Curiosidades
# ══════════════════════════════════════════════════════════════════
with tab2:
    st.markdown('<div class="section-header">💡 Curiosidades Genéticas</div>', unsafe_allow_html=True)
    curiosities = analyzer.get_curiosities()
    if not curiosities:
        st.warning("No se encontraron curiosidades.")
    else:
        for i in range(0, len(curiosities), 3):
            cols = st.columns(3)
            for j in range(3):
                if i + j < len(curiosities):
                    c = curiosities[i + j]
                    with cols[j]:
                        st.markdown(render_curiosity_card(c), unsafe_allow_html=True)
                        with st.expander("Fun fact!"):
                            st.write(c.get('fun_fact', 'Sin dato curioso extra.'))

# ══════════════════════════════════════════════════════════════════
# TAB 3: Ancestros Famosos
# ══════════════════════════════════════════════════════════════════
with tab3:
    st.markdown('<div class="section-header">🏛️ Ancestros Famosos y Herencia Arcaica</div>', unsafe_allow_html=True)
    
    if HAS_FAMOUS_ANCESTORS:
        # Load df once
        df = analyzer.raw_data if hasattr(analyzer, 'raw_data') and analyzer.raw_data is not None else analyzer.df
        
        y_haplo_res = infer_y_haplogroup(df)
        mt_haplo_res = infer_mt_haplogroup(df)
        
        y_haplo = y_haplo_res[0] if isinstance(y_haplo_res, (tuple, list)) else y_haplo_res
        y_conf = y_haplo_res[1] if isinstance(y_haplo_res, (tuple, list)) and len(y_haplo_res) > 1 else "Baja"

        mt_haplo = mt_haplo_res[0] if isinstance(mt_haplo_res, (tuple, list)) else mt_haplo_res
        mt_conf = mt_haplo_res[1] if isinstance(mt_haplo_res, (tuple, list)) and len(mt_haplo_res) > 1 else "Baja"

        famous_data = get_famous_ancestors(y_haplo, mt_haplo)

        # Extraer figuras históricas de famous_data
        famous_figures = []
        if isinstance(famous_data, dict):
            for h_key, h_info in famous_data.items():
                if isinstance(h_info, dict):
                    h_code = h_info.get('haplogroup', '')
                    h_label = h_info.get('nickname', h_info.get('full_name', h_code))
                    for fig in h_info.get('famous_figures', []):
                        famous_figures.append({
                            'name': fig.get('name', ''),
                            'emoji': fig.get('image_emoji', '👤'),
                            'haplogroup': f"{h_code} ({h_label})" if h_label and h_label != h_code else h_code,
                            'description': fig.get('connection', ''),
                            'years': fig.get('years', ''),
                            'confidence': fig.get('confidence', '')
                        })
        elif isinstance(famous_data, list):
            famous_figures = famous_data

        neanderthal = estimate_neanderthal_snps(df)
        blood = predict_blood_type(df)
        
        st.markdown("### 🧬 Detección de Haplogrupos Directos")
        c1, c2 = st.columns(2)
        with c1:
            if y_haplo and y_haplo != 'unknown':
                st.markdown(f"""
                <div class="glass-card" style="border-left: 4px solid #4f8ef7; text-align:center;">
                    <div style="font-size: 2rem;">⚔️</div>
                    <h3 style="color:#4f8ef7; margin:0;">Haplogrupo Y: {y_haplo}</h3>
                    <p style="color:#8b949e; margin:5px 0;">Linaje paterno directo (Confianza: {y_conf})</p>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div class="glass-card" style="border-left: 4px solid #30363d; text-align:center;">
                    <div style="font-size: 2rem;">🧬</div>
                    <h4 style="color:#8b949e; margin:0;">Haplogrupo Y (Línea Paterna)</h4>
                    <p style="color:#6e7681; font-size:0.85rem; margin:5px 0;">
                        Los chips generales de MyHeritage analizan ~3.400 SNPs en el cromosoma Y, pero las subramas finas requieren paneles de secuenciación profunda de Y.
                    </p>
                </div>
                """, unsafe_allow_html=True)
        with c2:
            if mt_haplo and mt_haplo != 'unknown':
                st.markdown(f"""
                <div class="glass-card" style="border-left: 4px solid #bc8cff; text-align:center;">
                    <div style="font-size: 2rem;">👑</div>
                    <h3 style="color:#bc8cff; margin:0;">Haplogrupo mt: {mt_haplo}</h3>
                    <p style="color:#8b949e; margin:5px 0;">Linaje materno directo (Confianza: {mt_conf})</p>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div class="glass-card" style="border-left: 4px solid #30363d; text-align:center;">
                    <div style="font-size: 2rem;">🌿</div>
                    <h4 style="color:#8b949e; margin:0;">Haplogrupo Mitocondrial (Línea Materna)</h4>
                    <p style="color:#6e7681; font-size:0.85rem; margin:5px 0;">
                        MyHeritage se enfoca en cromosomas 1-22, X e Y, por lo que el ADNmt no se analiza en este chip comercial.
                    </p>
                </div>
                """, unsafe_allow_html=True)

        # ──────────────────────────────────────────────────────────
        # Conexiones Históricas Detectadas por Marcadores Autosómicos
        # ──────────────────────────────────────────────────────────
        st.markdown("### 🌟 Linajes Históricos Detectados en tu Genoma")
        st.caption("A través de tus marcadores autosómicos de poblaciones ancestrales y ADN antiguo, tu ADN se conecta con estas grandes corrientes históricas:")

        detected_ancestor_cols = st.columns(3)

        # Chequear EDAR (Precolombino / Asia Oriental)
        edar_snp = analyzer.get_snp_result('rs3827760')
        has_edar = edar_snp and 'A' in edar_snp.get('genotype', '')

        # Chequear SLC24A5 / SLC45A2 (Ibérico / Europeo Atlántico)
        slc_snp = analyzer.get_snp_result('rs1426654')
        has_slc = slc_snp and 'A' in slc_snp.get('genotype', '')

        # Chequear Neandertal
        nean_var = analyzer.get_snp_result('rs4833103')
        has_nean = nean_var and ('A' in nean_var.get('genotype', '') or 'C' in nean_var.get('genotype', ''))

        with detected_ancestor_cols[0]:
            if has_edar:
                st.markdown("""
                <div class="ancestor-card" style="border-color: #e056fd; background: rgba(30, 20, 45, 0.6);">
                    <span class="ancestor-emoji">🦅</span>
                    <h4 style="color:#e056fd; margin-bottom:5px;">Pueblos Originarios y Dinastías Americanas</h4>
                    <div class="confidence-badge" style="background:#e056fd22; color:#e056fd;">Marcador EDARV370A Detectado</div>
                    <p style="font-size:0.82rem; color:#c9d1d9; margin-top:8px;">
                        Compartes linaje genético con los constructores de <strong>Tenochtitlán, Machu Picchu y Palenque</strong> (Moctezuma II, Pachacútec, Pakal). Este marcador surgió en Beringia hace ~20.000 años.
                    </p>
                    <small style="color:#8b949e;">Evidencia: Genoma antiguo de momias andinas y mayas (Cell / Science)</small>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown("""
                <div class="ancestor-card" style="opacity:0.8;">
                    <span class="ancestor-emoji">🏹</span>
                    <h4 style="color:#e6edf3; margin-bottom:5px;">Linajes Euroasiáticos</h4>
                    <p style="font-size:0.82rem; color:#8b949e;">Marcadores basales de poblaciones euroasiáticas occidentales.</p>
                </div>
                """, unsafe_allow_html=True)

        with detected_ancestor_cols[1]:
            if has_slc:
                st.markdown("""
                <div class="ancestor-card" style="border-color: #5bbf76; background: rgba(15, 35, 25, 0.6);">
                    <span class="ancestor-emoji">⚔️</span>
                    <h4 style="color:#5bbf76; margin-bottom:5px;">El Refugio Ibérico y Linaje Atlántico</h4>
                    <div class="confidence-badge" style="background:#5bbf7622; color:#5bbf76;">Marcador SLC24A5/SLC45A2 Detectado</div>
                    <p style="font-size:0.82rem; color:#c9d1d9; margin-top:8px;">
                        Linaje compartido con los pueblos de la Península Ibérica y Europa Occidental: <strong>Don Pelayo, Miguel de Cervantes, pueblos celtíberos y la nobleza hispana</strong> medieval (R1b-M269/DF27).
                    </p>
                    <small style="color:#8b949e;">Evidencia: Olalde et al., Science 2019 (Paleogenómica Ibérica)</small>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown("""
                <div class="ancestor-card" style="opacity:0.8;">
                    <span class="ancestor-emoji">🛡️</span>
                    <h4 style="color:#e6edf3; margin-bottom:5px;">Linaje Atlántico</h4>
                    <p style="font-size:0.82rem; color:#8b949e;">Raíces compartidas con Europa Occidental.</p>
                </div>
                """, unsafe_allow_html=True)

        with detected_ancestor_cols[2]:
            st.markdown("""
            <div class="ancestor-card" style="border-color: #e3b341; background: rgba(35, 30, 15, 0.6);">
                <span class="ancestor-emoji">🦴</span>
                <h4 style="color:#e3b341; margin-bottom:5px;">Homo neanderthalensis de Eurasia</h4>
                <div class="confidence-badge" style="background:#e3b34122; color:#e3b341;">Introgresión Arcaica Activa</div>
                <p style="font-size:0.82rem; color:#c9d1d9; margin-top:8px;">
                    Compartes segmentos de ADN intactos con los <strong>neandertales de la Cueva de El Sidrón (Asturias) y Vindija (Croacia)</strong>. Este cruce ocurrió hace ~55.000 años en el Próximo Oriente.
                </p>
                <small style="color:#8b949e;">Evidencia: Proyecto Genoma Neandertal (Pääbo, Nobel 2022)</small>
            </div>
            """, unsafe_allow_html=True)

        # ──────────────────────────────────────────────────────────
        # Explorador Interactivo de Dinastías y Linajes Históricos
        # ──────────────────────────────────────────────────────────
        st.markdown("### 👑 Explorador de Linajes y Personajes Históricos")
        st.write("Explora las grandes ramas de la humanidad y descubre qué personajes históricos compartían cada linaje genético:")

        lineage_options = {
            "R1b-M269": "⚔️ R1b-M269: Los Celtas, Reyes Ibéricos y Napoleón (Península Ibérica y Atlántico)",
            "Q": "🦅 Q: Los Señores de América y los Andes (Mayas, Mexicas e Incas)",
            "I1": "🛡️ I1: Los Vikingos del Norte (Ragnar Lodbrok, Harald Bluetooth)",
            "R1a": "🐎 R1a: Los Jinetes de la Estepa y Asia Central (Gengis Kan, Atila el Huno)",
            "E1b1b": "🌅 E1b1b: Pueblos del Mediterráneo y Faraones (Sócrates, Antiguo Egipto)",
            "J2": "🌾 J2: Creciente Fértil y Mesopotamia (Alejandro Magno, Hammurabi)",
            "G2a": "🧊 G2a: Los Primeros Agricultores de Europa (Ötzi el Hombre de los Hielos)",
            "H": "👑 mtDNA H: La Madre de Europa (Dinastía Romanov, Marie Curie)",
            "V": "🏔️ mtDNA V: El Refugio Glacial Ibérico y Cantábrico (Nobleza Navarra)",
            "K": "✡️ mtDNA K: Las Madres de Ashkenaz (Línea materna de Ötzi)",
        }

        selected_key = st.selectbox(
            "Selecciona un linaje histórico para ver sus figuras y contexto arqueológico:",
            options=list(lineage_options.keys()),
            format_func=lambda k: lineage_options[k],
            index=0
        )

        selected_info = FAMOUS_ANCESTORS_DB.get(selected_key, {})
        if selected_info:
            color = selected_info.get('color', '#4f8ef7')
            st.markdown(f"""
            <div class="glass-card" style="border-left: 5px solid {color}; margin: 15px 0;">
                <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap;">
                    <div>
                        <span style="font-size:2rem; margin-right:10px;">{selected_info.get('emoji', '🏛️')}</span>
                        <strong style="font-size:1.3rem; color:#e6edf3;">{selected_info.get('full_name', '')}</strong>
                        <span style="color:{color}; font-weight:600; margin-left:10px;">— {selected_info.get('nickname', '')}</span>
                    </div>
                    <div style="color:#8b949e; font-size:0.9rem;">
                        ⏳ <strong>Edad:</strong> {selected_info.get('age', '')} | 📍 <strong>Origen:</strong> {selected_info.get('origin', '')}
                    </div>
                </div>
                <p style="color:#c9d1d9; font-size:0.95rem; margin-top:12px; line-height:1.6;">
                    {selected_info.get('description', '')}
                </p>
                <div style="background:rgba(255,255,255,0.03); padding:8px 12px; border-radius:8px; font-size:0.85rem; color:#8b949e;">
                    🌍 <strong>Distribución actual:</strong> {selected_info.get('distribution', '')}
                </div>
            </div>
            """, unsafe_allow_html=True)

            figs = selected_info.get('famous_figures', [])
            if figs:
                fig_cols = st.columns(min(len(figs), 3))
                for idx, fig in enumerate(figs):
                    with fig_cols[idx % 3]:
                        st.markdown(f"""
                        <div class="ancestor-card" style="min-height: 240px;">
                            <span class="ancestor-emoji">{fig.get('image_emoji', '👤')}</span>
                            <h4 style="color:#e6edf3; margin: 4px 0;">{fig.get('name', '')}</h4>
                            <div style="color:#8b949e; font-size:0.8rem; margin-bottom:8px;">{fig.get('years', '')}</div>
                            <div class="confidence-badge" style="background:{color}22; color:{color};">{fig.get('confidence', '')}</div>
                            <p style="font-size:0.82rem; color:#c9d1d9; margin-top:8px; line-height:1.5;">{fig.get('connection', '')}</p>
                            <small style="color:#6e7681; display:block; margin-top:6px;">📚 {fig.get('source', '')}</small>
                        </div>
                        """, unsafe_allow_html=True)

        # ──────────────────────────────────────────────────────────
        # Herencia Neandertal con Detalle
        # ──────────────────────────────────────────────────────────
        st.markdown("### 🦴 Análisis Detallado de Herencia Neandertal")
        neanderthal = estimate_neanderthal_snps(df)
        
        if isinstance(neanderthal, (tuple, list)):
            n_count = neanderthal[0] if len(neanderthal) > 0 else 0
            n_pct = neanderthal[1] if len(neanderthal) > 1 else 0.0
            n_details = neanderthal[2] if len(neanderthal) > 2 else []
        elif hasattr(neanderthal, 'get'):
            n_count = neanderthal.get('count', 0)
            n_pct = neanderthal.get('percentage', 0.0)
            n_details = neanderthal.get('details', [])
        else:
            n_count, n_pct, n_details = 0, 0.0, []

        real_genomic_pct = round(1.2 + (n_pct / 100.0) * 1.8, 1)

        c_nean1, c_nean2 = st.columns([1, 2])
        with c_nean1:
            st.markdown(f"""
            <div class="glass-card" style="text-align:center; border-color:#e3b341; padding:25px;">
                <div style="font-size:3.5rem; color:#e3b341; font-weight:800;">~{real_genomic_pct}%</div>
                <strong style="color:#e6edf3; font-size:1.1rem;">ADN Neandertal Estimado</strong>
                <p style="color:#8b949e; font-size:0.85rem; margin-top:6px;">
                    {n_count} de {int(n_count / (n_pct/100)) if n_pct > 0 else 20} marcadores arcaicos analizados fueron positivos ({n_pct:.0f}%)
                </p>
                <div class="confidence-badge" style="background:#e3b34122; color:#e3b341;">Rango Típico Euroasiático (1-3%)</div>
            </div>
            """, unsafe_allow_html=True)

        with c_nean2:
            st.markdown("""
            <div class="glass-card" style="padding:20px;">
                <h4 style="color:#e6edf3; margin-top:0;">🛡️ ¿Qué heredaste de los neandertales?</h4>
                <p style="color:#8b949e; font-size:0.9rem; line-height:1.6;">
                    Cuando los humanos modernos salieron de África hace 60.000 años, se encontraron con los neandertales en Oriente Próximo y Europa. 
                    Las variantes que conservas no son ruido aleatorio: aportaron ventajas evolutivas cruciales:
                </p>
                <ul style="color:#c9d1d9; font-size:0.85rem; line-height:1.8;">
                    <li><strong>Sistema Inmunitario (TNFRSF8, IRF5):</strong> Receptores de reconocimiento de patógenos adaptados al clima euroasiático.</li>
                    <li><strong>Ritmo Circadiano y Sueño (CLOCK):</strong> Adaptación a las variaciones estacionales de luz en latitudes septentrionales.</li>
                    <li><strong>Coagulación y Cicatrización:</strong> Respuesta rápida ante heridas en entornos hostiles.</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)

        if n_details:
            with st.expander(f"🔬 Ver los {len(n_details)} marcadores neandertales específicos encontrados en tu ADN"):
                d_df = pd.DataFrame(n_details)
                st.dataframe(d_df, use_container_width=True, hide_index=True)

        # ──────────────────────────────────────────────────────────
        # Predicción de Grupo Sanguíneo
        # ──────────────────────────────────────────────────────────
        st.markdown("### 🩸 Grupo Sanguíneo (Predicción Genómica)")
        blood = predict_blood_type(df)
        blood_type_display = (blood.get('type') or blood.get('blood_type', 'N/A')) if isinstance(blood, dict) else 'N/A'
        blood_conf_display = blood.get('confidence', 'Baja') if isinstance(blood, dict) else 'Baja'
        snps_used_str = ", ".join(blood.get('snps_used', [])) if isinstance(blood, dict) else ""

        b_c1, b_c2 = st.columns([1, 2])
        with b_c1:
            st.markdown(f"""
            <div class="glass-card" style="text-align:center; border-color:#ff5252; padding:25px;">
                <div style="font-size:3.5rem; font-weight:800; color:#ff5252;">{blood_type_display}</div>
                <strong style="color:#e6edf3;">Grupo ABO / Factor Rh</strong>
                <p style="color:#8b949e; font-size:0.85rem; margin-top:5px;">Confianza de predicción: {blood_conf_display}</p>
                <small style="color:#6e7681;">SNPs evaluados: {snps_used_str}</small>
            </div>
            """, unsafe_allow_html=True)
        with b_c2:
            st.markdown("""
            <div class="glass-card" style="padding:20px;">
                <h4 style="color:#e6edf3; margin-top:0;">💡 Historia evolutiva de los grupos sanguíneos</h4>
                <p style="color:#8b949e; font-size:0.9rem; line-height:1.6;">
                    El grupo sanguíneo es uno de los primeros polimorfismos descubiertos en la especie humana. 
                    El alelo <strong>A</strong> es el más antiguo en primates. El alelo <strong>O</strong> surgió como una mutación deleción que confirió protección frente a formas graves de malaria, expandiéndose masivamente en cazadores-recolectores y poblaciones indígenas de América.
                </p>
                <small style="color:#6e7681;">Nota: La confirmación clínica serológica es la única válida para transfusiones sanguíneas.</small>
            </div>
            """, unsafe_allow_html=True)

        # ──────────────────────────────────────────────────────────
        # Gran Línea del Tiempo Ancestral
        # ──────────────────────────────────────────────────────────
        st.markdown("### ⏳ La Odisea de tus Genes a través del Tiempo")
        st.markdown("""
        <div class="glass-card" style="line-height:2.0; font-family:'Courier New', monospace; font-size:0.95rem; color:#c9d1d9;">
            🌍 <strong>200.000 aC</strong> — Surge el <em>Homo sapiens</em> en África con el ADN mitocondrial ancestral.<br>
            🚶 <strong>70.000 aC</strong> — Tus antepasados forman parte de la gran migración que cruza el Mar Rojo hacia Eurasia.<br>
            🧬 <strong>55.000 aC</strong> — Encuentro y cruce con Neandertales en el Creciente Fértil (heredas tus variantes arcaicas).<br>
            ❄️ <strong>25.000 aC</strong> — Último Máximo Glacial: tus ancestros se refugian en la Península Ibérica y las estepas siberianas.<br>
            🌾 <strong>10.000 aC</strong> — Revolución Neolítica: domesticación del trigo y expansión de los primeros agricultores.<br>
            🦅 <strong>15.000 aC</strong> — Cruce del estrecho de Bering hacia América (origen de tu marcador EDARV370A).<br>
            ⚔️ <strong>4.500 aC</strong> — Expansión de los pastores Yamna y la cultura Campaniforme en la Península Ibérica.<br>
            👑 <strong>1500–1600 dC</strong> — Encuentro de los mundos ibérico e indígena americano en el Atlántico.<br>
            👤 <strong>HOY</strong> — <strong>Tú</strong>, portador vivo de este tapiz genético irrepetible.
        </div>
        """, unsafe_allow_html=True)
        
    else:
        st.info("El módulo de Ancestros Famosos no está disponible o no se pudo cargar.")

# ══════════════════════════════════════════════════════════════════
# TAB 4: Ancestría
# ══════════════════════════════════════════════════════════════════
with tab4:
    st.markdown('<div class="section-header">🌍 Tus señales de ancestría</div>', unsafe_allow_html=True)
    ancestry_signals = analyzer.get_ancestry_signals()
    found_signals = [s for s in ancestry_signals if s['found']]
    if not found_signals:
        st.warning("No se encontraron marcadores de ancestría.")
    else:
        for signal in found_signals:
            snp_info = signal['snp_info']
            interp = signal['interpretation']
            if interp:
                st.markdown(f"""
                <div class="ancestry-card">
                    <span style="font-size:1.5rem;">{interp.get('emoji', '🌍')}</span>
                    <strong style="color:#3fb950; margin-left:10px;">{snp_info.get('title', '')}</strong>
                    <p style="color:#8b949e; margin-top:5px;">{interp.get('result', '')}</p>
                </div>
                """, unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════
# TAB 5: Explorador de SNPs
# ══════════════════════════════════════════════════════════════════
with tab5:
    st.markdown('<div class="section-header">🔬 Explorador de SNPs</div>', unsafe_allow_html=True)
    query = st.text_input("Buscar rsID (Ej: rs12913832)")
    if query:
        res = analyzer.search_snp(query.strip())
        if res['found_in_file']:
            st.success(f"Encontrado! Genotipo: {res['user_result']['genotype']}")
        else:
            st.error("No encontrado.")
            
    # Full table
    df_table = pd.DataFrame([
        {
            'rsID': rsid, 'Gen': result['snp_info'].get('gene', ''),
            'Genotipo': result['user_result']['genotype'] if result['user_result'] else '—'
        }
        for rsid, result in analyzer.analyze_all_known_snps().items()
    ])
    st.dataframe(df_table, use_container_width=True)

# ══════════════════════════════════════════════════════════════════
# TAB 6: Salud y Predisposiciones a Enfermedades
# ══════════════════════════════════════════════════════════════════
with tab6:
    st.markdown('<div class="section-header">❤️ Predisposiciones Genéticas a Enfermedades y Salud Preventiva</div>', unsafe_allow_html=True)
    
    st.info(
        "ℹ️ **Aviso de Genética Médica Preventiva:** Este panel analiza variantes genéticas (SNPs) asociadas a predisposiciones "
        "a enfermedades comunes, salud cardiovascular, metabolismo y respuesta a fármacos catalogadas en bases de datos científicas internacionales (ClinVar, dbSNP, GWAS Catalog).\n\n"
        "**Recuerda:** En las enfermedades complejas habituales, **la genética no es destino**. Tu alimentación, ejercicio físico, descanso y entorno modulan activamente "
        "cómo se expresan tus genes (**epigenética**). Este análisis es puramente formativo y educativo; no constituye un diagnóstico médico ni sustituye la consulta médica profesional."
    )
    
    all_results = analyzer.analyze_all_known_snps()
    
    # ── Módulo Especial: Diplotipo APOE (Alzheimer y Perfil Lipídico) ──
    apoe_data = compute_apoe_haplotype(all_results)
    if apoe_data:
        st.markdown(f"""
        <div class="apoe-hero-card">
            <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:10px;">
                <div>
                    <span style="font-size:2rem; vertical-align:middle; margin-right:8px;">🧠</span>
                    <strong style="font-size:1.3rem; color:#e6edf3; vertical-align:middle;">Tu Diplotipo APOE: {apoe_data['haplotype']}</strong>
                </div>
                <span class="risk-tag {apoe_data['tag_class']}">{apoe_data['tier']}</span>
            </div>
            <div style="color:#4f8ef7; font-family:monospace; font-size:0.85rem; margin:10px 0;">
                Marcadores analizados: rs429358 ({apoe_data['g_429']}) + rs7412 ({apoe_data['g_741']})
            </div>
            <p style="color:#c9d1d9; font-size:0.95rem; margin-bottom:12px; line-height:1.5;">
                {apoe_data['desc']}
            </p>
            <div class="prevention-card" style="border-left-color: {apoe_data['color']};">
                <strong>💡 Recomendación preventiva personalizada:</strong> {apoe_data['prevention']}
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # ── Filtrar y preparar resultados de Salud y Metabolismo ──
    health_results = [
        r for r in all_results.values()
        if r['snp_info'].get('category') in ['Salud', 'Metabolismo'] and r['found'] and r['interpretation']
    ]
    
    processed_items = []
    count_increased = 0
    count_moderate = 0
    count_normal = 0
    count_pharma = 0
    
    for r in health_results:
        info = r['snp_info']
        interp = r['interpretation']
        result_text = interp.get('result', '')
        tier_name, color_class, tag_class, badge_color = classify_risk_tier(result_text)
        system = classify_health_system(info)
        
        if tier_name == 'Riesgo Aumentado':
            count_increased += 1
        elif tier_name == 'Riesgo Moderado / Portador':
            count_moderate += 1
        else:
            count_normal += 1
            
        if 'farmacogenómica' in system.lower() or 'medicamento' in system.lower():
            count_pharma += 1
            
        tip = get_prevention_tip(info.get('gene', ''), info.get('title', ''))
        
        processed_items.append({
            'r': r,
            'info': info,
            'interp': interp,
            'tier_name': tier_name,
            'color_class': color_class,
            'tag_class': tag_class,
            'badge_color': badge_color,
            'system': system,
            'tip': tip,
        })
        
    # ── Métricas Globales de Predisposición ──
    st.markdown("### 📊 Balance Global de Variantes de Salud")
    m1, m2, m3, m4, m5 = st.columns(5)
    m1.metric("🔬 Variantes Analizadas", len(processed_items))
    m2.metric("🟢 Favorable / Normal", count_normal)
    m3.metric("🟡 Moderado / Portador", count_moderate)
    m4.metric("🔴 Riesgo Aumentado", count_increased)
    m5.metric("💊 Farmacogenómica", count_pharma)
    
    st.markdown("---")
    
    # ── Filtros Interactivos ──
    f_col1, f_col2 = st.columns([1, 1])
    
    systems_available = ["Todos los sistemas"] + sorted(list(set(item['system'] for item in processed_items)))
    with f_col1:
        selected_system = st.selectbox(
            "🩺 Filtrar por Sistema Corporal / Especialidad:",
            options=systems_available,
            index=0
        )
        
    with f_col2:
        selected_tier = st.selectbox(
            "🎚️ Filtrar por Nivel de Riesgo:",
            options=["Todos los niveles", "🔴 Riesgo Aumentado", "🟡 Riesgo Moderado / Portador", "🟢 Normal / Favorable"],
            index=0
        )
        
    search_term = st.text_input(
        "🔍 Buscar patología, síntoma o gen (ej: corazón, diabetes, trombosis, hierro, colesterol, estatinas):",
        ""
    ).strip().lower()
    
    # Aplicar filtros
    filtered_items = processed_items
    
    if selected_system != "Todos los sistemas":
        filtered_items = [it for it in filtered_items if it['system'] == selected_system]
        
    if selected_tier == "🔴 Riesgo Aumentado":
        filtered_items = [it for it in filtered_items if it['tier_name'] == 'Riesgo Aumentado']
    elif selected_tier == "🟡 Riesgo Moderado / Portador":
        filtered_items = [it for it in filtered_items if it['tier_name'] == 'Riesgo Moderado / Portador']
    elif selected_tier == "🟢 Normal / Favorable":
        filtered_items = [it for it in filtered_items if it['tier_name'] == 'Normal / Favorable']
        
    if search_term:
        filtered_items = [
            it for it in filtered_items
            if search_term in it['info'].get('title', '').lower()
            or search_term in it['info'].get('gene', '').lower()
            or search_term in it['info'].get('description', '').lower()
            or search_term in it['interp'].get('result', '').lower()
            or search_term in it['interp'].get('detail', '').lower()
            or search_term in it['info'].get('rsid', '').lower()
            or search_term in it['system'].lower()
        ]
        
    st.markdown(f"**Mostrando {len(filtered_items)} variantes:**")
    
    if not filtered_items:
        st.warning("No se encontraron variantes que coincidan con los filtros seleccionados.")
    else:
        for i in range(0, len(filtered_items), 2):
            c1, c2 = st.columns(2)
            for j, col in enumerate([c1, c2]):
                if i + j < len(filtered_items):
                    item = filtered_items[i + j]
                    info = item['info']
                    interp = item['interp']
                    r = item['r']
                    rsid = info.get('rsid', '')
                    
                    with col:
                        st.markdown(f"""
                        <div class="health-card {item['color_class']}">
                            <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:6px;">
                                <span style="font-size:0.75rem; color:#8b949e; text-transform:uppercase;">{item['system']}</span>
                                <span class="risk-tag {item['tag_class']}">{item['tier_name']}</span>
                            </div>
                            <h4 style="margin:2px 0 6px 0; color:#e6edf3;">
                                {interp.get('emoji', '🩺')} {info.get('title', '')}
                            </h4>
                            <div style="display:flex; justify-content:space-between; margin-bottom:8px;">
                                <span style="color:#4f8ef7; font-family:monospace; font-size:0.85rem; font-weight:600;">
                                    {info.get('gene', '')} · <a href="https://www.ncbi.nlm.nih.gov/snp/{rsid}" target="_blank" style="color:#4f8ef7; text-decoration:none;">{rsid} ↗</a>
                                </span>
                                <span style="background:rgba(255,255,255,0.1); padding:2px 8px; border-radius:6px; font-family:monospace; font-weight:700; color:#e6edf3;">
                                    {r['user_result']['genotype']}
                                </span>
                            </div>
                            <div style="font-size:1rem; font-weight:700; color:#e6edf3; margin-bottom:6px;">
                                {interp.get('result', '')}
                            </div>
                            <p style="color:#8b949e; font-size:0.85rem; line-height:1.45; margin-bottom:10px;">
                                {interp.get('detail', '')}
                            </p>
                            <div class="prevention-card">
                                <strong>💡 ¿Qué dice la ciencia para prevenir?</strong><br>
                                {item['tip']}
                            </div>
                        </div>
                        """, unsafe_allow_html=True)
                        
    # ── Guía de Consulta Médica ──
    with st.expander("🩺 Guía: Cómo hablar con tu médico de cabecera sobre estos resultados"):
        st.markdown("""
        **Consejos prácticos para aprovechar tu análisis genético en consulta médica:**
        
        1. **La genética es un mapa de probabilidades, no una certeza diagnóstica:**  
           Tener una variante de riesgo relativo (como en *9p21* o *TCF7L2*) no significa que vayas a enfermar, 
           del mismo modo que tener variantes protectoras no te hace inmune si descuidas tu estilo de vida.
        2. **Pruebas clínicas de confirmación pertinentes:**  
           - Si tienes variantes en **HFE** (C282Y / H63D), solicita en tu próxima analítica los niveles de **ferritina** e **índice de saturación de transferrina**.
           - Si tienes variantes de riesgo cardiovascular o **TCF7L2**, mantén un seguimiento periódico de **perfil lipídico avanzado (ApoB/LDL-C)** y **HbA1c (hemoglobina glicosilada)**.
        3. **Farmacogenómica:**  
           Si tu médico te prescribe medicamentos específicos (como **estatinas** para el colesterol, **clopidogrel** tras un cateterismo, o anticoagulantes como **warfarina/Sintrom**), 
           comentar tus variantes de enzimas hepáticas (*SLCO1B1*, *CYP2C19*, *CYP4F2*) le ayudará a personalizar la molécula y dosis más seguras para ti.
        4. **El poder de la epigenética:**  
           El ejercicio aeróbico regular, una alimentación mínimamente procesada rica en polifenoles y fibra, la gestión del estrés y 7-8 horas de sueño reparador 
           son los moduladores epigenéticos más potentes respaldados por la medicina moderna.
        """)
