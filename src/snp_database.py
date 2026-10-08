"""
snp_database.py
---------------
Base de datos hardcoded con más de 80 SNPs conocidos.
Cubre rasgos físicos, salud, metabolismo y ancestría.
Todo el contenido está en ESPAÑOL.

Cada entrada tiene:
  - rsid: identificador del SNP
  - gene: gen asociado
  - category: Rasgo / Salud / Metabolismo / Ancestría
  - subcategory: subcategoría específica
  - title: título en español
  - description: descripción detallada en español
  - interpretations: dict con genotipo -> {result, emoji, detail}
  - fun_fact: curiosidad divertida en español
"""

SNP_DATABASE = {

    # ────────────────────────────────────────────────────────────────
    # RASGOS FÍSICOS
    # ────────────────────────────────────────────────────────────────

    'rs12913832': {
        'rsid': 'rs12913832',
        'gene': 'HERC2/OCA2',
        'category': 'Rasgo',
        'subcategory': 'Color de ojos',
        'title': 'Color de ojos',
        'description': (
            'Este SNP en el gen HERC2/OCA2 es el principal determinante del color de ojos humano. '
            'La variante A reduce la expresión de OCA2, disminuyendo la producción de melanina en el iris, '
            'lo que resulta en ojos azules o verdes. La variante G favorece ojos marrones oscuros.'
        ),
        'interpretations': {
            'AA': {'result': 'Ojos azules', 'emoji': '🔵', 'detail': 'Muy probablemente ojos azules o grises. Alta probabilidad de herencia nórdica o centroeuropea.'},
            'AG': {'result': 'Ojos verdes o avellana', 'emoji': '🟢', 'detail': 'Resultado intermedio. Los ojos pueden ser verdes, avellana o azul-verdosos.'},
            'GG': {'result': 'Ojos marrones', 'emoji': '🟤', 'detail': 'El alelo G favorece la producción de melanina. Ojos oscuros muy probables.'},
        },
        'fun_fact': '¡Solo el 8% de la población mundial tiene ojos azules! Este rasgo surgió hace apenas 6.000-10.000 años en una sola persona cerca del mar Báltico. 👁️'
    },

    'rs1805007': {
        'rsid': 'rs1805007',
        'gene': 'MC1R',
        'category': 'Rasgo',
        'subcategory': 'Color de cabello',
        'title': 'Cabello rojo (gen MC1R)',
        'description': (
            'El gen MC1R (receptor de melanocortina 1) controla el tipo de melanina producida en los melanocitos. '
            'La variante T reduce la eficiencia del receptor, desviando la producción hacia feomelanina (roja/amarilla) '
            'en lugar de eumelanina (marrón/negra). Portadores de dos copias T suelen tener cabello rojo y piel muy clara.'
        ),
        'interpretations': {
            'CC': {'result': 'Sin variante MC1R', 'emoji': '🖤', 'detail': 'Receptor MC1R funcional. Producción normal de eumelanina. Cabello oscuro muy probable.'},
            'CT': {'result': 'Portador de variante roja', 'emoji': '🟠', 'detail': 'Un alelo T. Puede haber reflejos cobrizos o pelirrojos leves, especialmente con otro alelo MC1R.'},
            'TT': {'result': 'Alta probabilidad de cabello rojo', 'emoji': '🔴', 'detail': 'Dos alelos T. Muy probable cabello rojo o cobrizo, piel clara y sensibilidad aumentada al sol.'},
        },
        'fun_fact': 'Los pelirrojos necesitan hasta un 20% más de anestesia durante cirugías. Su umbral del dolor también es diferente, según estudios de la Universidad de Louisville. 🏥'
    },

    'rs1042602': {
        'rsid': 'rs1042602',
        'gene': 'TYR',
        'category': 'Rasgo',
        'subcategory': 'Pigmentación',
        'title': 'Pigmentación de la piel (TYR)',
        'description': (
            'El gen TYR codifica la tirosinasa, enzima clave en la síntesis de melanina. '
            'La variante C en rs1042602 está asociada a menor actividad de la tirosinasa, '
            'reduciendo la producción de melanina y resultando en piel más clara.'
        ),
        'interpretations': {
            'AA': {'result': 'Piel más oscura', 'emoji': '🌿', 'detail': 'Alelo A asociado a mayor actividad TYR y más melanina. Buena protección solar natural.'},
            'AC': {'result': 'Pigmentación intermedia', 'emoji': '🌻', 'detail': 'Combinación de ambos alelos. Pigmentación variable dependiendo de otros genes.'},
            'CC': {'result': 'Piel más clara', 'emoji': '🌸', 'detail': 'El alelo C reduce la actividad de la tirosinasa. Mayor sensibilidad a la radiación UV.'},
        },
        'fun_fact': 'La variación en el color de piel humana es principalmente resultado de la presión selectiva de la radiación solar UV a lo largo de la historia evolutiva. ☀️'
    },

    'rs4988235': {
        'rsid': 'rs4988235',
        'gene': 'MCM6/LCT',
        'category': 'Rasgo',
        'subcategory': 'Digestión',
        'title': 'Tolerancia a la lactosa',
        'description': (
            'Este SNP controla si el gen de la lactasa (LCT) permanece activo en la edad adulta. '
            'El alelo A es una variante de persistencia de la lactasa: el gen LCT sigue activo '
            'toda la vida, permitiendo digerir la leche sin problemas. '
            'El alelo G implica que la lactasa se "apaga" normalmente tras la infancia.'
        ),
        'interpretations': {
            'AA': {'result': 'Tolerante a la lactosa', 'emoji': '🥛', 'detail': 'Dos copias de la variante europea de persistencia. Puedes tomar productos lácteos sin problema.'},
            'AG': {'result': 'Tolerancia parcial', 'emoji': '🧀', 'detail': 'Una copia. Probablemente tolerante, pero grandes cantidades de lactosa pueden causar leve malestar.'},
            'GG': {'result': 'Intolerancia a la lactosa', 'emoji': '🚫', 'detail': 'Sin variante de persistencia. La lactasa se reduce con la edad. Los lácteos pueden causar molestias digestivas.'},
        },
        'fun_fact': 'El 65% de la humanidad es intolerante a la lactosa en la edad adulta. La tolerancia es una mutación surgida hace ~10.000 años en Europa cuando comenzó la ganadería. 🐄'
    },

    'rs1726866': {
        'rsid': 'rs1726866',
        'gene': 'TAS2R38',
        'category': 'Rasgo',
        'subcategory': 'Percepción del gusto',
        'title': 'Percepción del sabor amargo',
        'description': (
            'El gen TAS2R38 codifica un receptor gustativo para el sabor amargo. '
            'La variante T (alelo PAV) produce un receptor funcional que detecta compuestos '
            'amargos como PTC/PROP. Las personas con este alelo son "supertasters" para lo amargo. '
            'El alelo C (AVI) produce un receptor no funcional.'
        ),
        'interpretations': {
            'TT': {'result': 'Supertaster del amargo', 'emoji': '😖', 'detail': 'Muy sensible al sabor amargo. Verduras como el brócoli, las coles de Bruselas o el café sin azúcar pueden resultar muy intensos.'},
            'CT': {'result': 'Sensibilidad moderada', 'emoji': '😐', 'detail': 'Portador de un alelo funcional. Sensibilidad al amargo intermedia.'},
            'CC': {'result': 'No percibe el amargo', 'emoji': '😋', 'detail': 'Sin receptor funcional. Los sabores amargos son menos intensos. Mayor probabilidad de disfrutar café y cerveza amarga.'},
        },
        'fun_fact': 'Los "supertasters" tienen hasta 4 veces más papilas gustativas que la media. ¡También son más propensos a rechazar verduras amargas que son muy saludables! 🥦'
    },

    'rs713598': {
        'rsid': 'rs713598',
        'gene': 'OR6A2',
        'category': 'Rasgo',
        'subcategory': 'Percepción del gusto',
        'title': 'Cilantro: ¿hierba o jabón?',
        'description': (
            'El gen OR6A2 codifica un receptor olfativo que detecta aldehídos, '
            'compuestos que abundan tanto en el cilantro como en el jabón. '
            'Las personas con el alelo C perciben el cilantro como jabonoso o desagradable '
            'en lugar de fresco y aromático.'
        ),
        'interpretations': {
            'CC': {'result': 'Cilantro sabe a jabón', 'emoji': '🧼', 'detail': 'Tienes el alelo que activa OR6A2 ante los aldehídos del cilantro. ¡Para ti sabe a jabón de lavar!'},
            'CG': {'result': 'Percepción mixta', 'emoji': '🌿', 'detail': 'Un alelo C. Puede haber alguna nota jabonosa en el cilantro, pero no tan intensa.'},
            'GG': {'result': 'Cilantro sabe normal', 'emoji': '✅', 'detail': 'Sin el alelo problemático. El cilantro te resulta fresco y aromático como a la mayoría.'},
        },
        'fun_fact': 'Entre el 4% y el 14% de la población percibe el cilantro como jabón. Julia Child, famosa chef americana, lo odiaba y lo tiraba por el suelo. 🌿'
    },

    'rs6265': {
        'rsid': 'rs6265',
        'gene': 'BDNF',
        'category': 'Rasgo',
        'subcategory': 'Memoria y aprendizaje',
        'title': 'Memoria y plasticidad cerebral (BDNF)',
        'description': (
            'El gen BDNF (Factor Neurotrófico Derivado del Cerebro) regula la supervivencia neuronal, '
            'la formación de conexiones sinápticas y la memoria episódica. '
            'La variante Met (A) en rs6265 produce una proteína BDNF con menor secreción '
            'en respuesta a la actividad neuronal, lo que puede afectar la memoria declarativa.'
        ),
        'interpretations': {
            'GG': {'result': 'Memoria óptima', 'emoji': '🧠', 'detail': 'Alelo Val/Val. Secreción normal de BDNF. Plasticidad sináptica y memoria episódica óptimas.'},
            'AG': {'result': 'Memoria ligeramente reducida', 'emoji': '💡', 'detail': 'Val/Met. Secreción de BDNF algo reducida. Aún funciona bien en condiciones normales.'},
            'AA': {'result': 'Variante Met/Met', 'emoji': '📝', 'detail': 'Alelo Met/Met. Menor liberación de BDNF. Ligera reducción en memoria episódica. El ejercicio físico puede compensarlo.'},
        },
        'fun_fact': 'El ejercicio aeróbico incrementa la producción de BDNF hasta un 300%. ¡Correr es literalmente hacer crecer el cerebro! 🏃'
    },

    'rs1799971': {
        'rsid': 'rs1799971',
        'gene': 'OPRM1',
        'category': 'Rasgo',
        'subcategory': 'Sensibilidad al dolor',
        'title': 'Sensibilidad al dolor (OPRM1)',
        'description': (
            'El gen OPRM1 codifica el receptor mu-opioide, el principal receptor al que se une '
            'la morfina y las endorfinas naturales del cuerpo. '
            'La variante G en rs1799971 produce un receptor con mayor afinidad por los opioides, '
            'lo que puede resultar en mayor sensibilidad al dolor y también mayor recompensa social.'
        ),
        'interpretations': {
            'AA': {'result': 'Sensibilidad al dolor normal', 'emoji': '😊', 'detail': 'Receptor mu-opioide estándar. Respuesta al dolor y a los analgésicos típica.'},
            'AG': {'result': 'Mayor sensibilidad al dolor', 'emoji': '⚡', 'detail': 'Un alelo G. Receptor con mayor afinidad. Puede haber mayor sensibilidad al dolor físico y social.'},
            'GG': {'result': 'Alta sensibilidad al dolor', 'emoji': '🔥', 'detail': 'Dos alelos G. Receptor muy sensible. Más sensible al dolor, pero también a las recompensas sociales y al placer.'},
        },
        'fun_fact': 'Las personas con el alelo G sufren más con el rechazo social: el mismo sistema opioide que procesa el dolor físico también procesa el dolor de la exclusión social. 💔'
    },

    'rs1815739': {
        'rsid': 'rs1815739',
        'gene': 'ACTN3',
        'category': 'Rasgo',
        'subcategory': 'Rendimiento atlético',
        'title': 'Gen del atleta (ACTN3)',
        'description': (
            'El gen ACTN3 codifica la alfa-actinina-3, una proteína estructural exclusiva de '
            'las fibras musculares de contracción rápida (tipo II). '
            'El alelo C (R577X) introduce un codón de parada prematuro, '
            'eliminando la producción de ACTN3. '
            'Los portadores de CC tienen predominio de fibras lentas (mejor resistencia), '
            'mientras que los TT tienen fibras rápidas (mejor potencia y velocidad).'
        ),
        'interpretations': {
            'TT': {'result': 'Perfil de potencia/velocidad', 'emoji': '⚡', 'detail': 'ACTN3 funcional en ambas copias. Más fibras rápidas. Ventaja en deportes explosivos: sprint, halterofilia, salto.'},
            'CT': {'result': 'Perfil mixto', 'emoji': '🏊', 'detail': 'Una copia funcional. Buena combinación de potencia y resistencia. Apto para deportes de equipo y mixtos.'},
            'CC': {'result': 'Perfil de resistencia', 'emoji': '🏃', 'detail': 'Sin ACTN3 funcional. Predominio de fibras lentas. Ventaja en maratón, ciclismo de fondo, deportes de resistencia.'},
        },
        'fun_fact': 'El alelo R (T) está prácticamente ausente en atletas élite de maratón kenianos, pero es muy frecuente en velocistas olímpicos. ¡Tu genoma ya sabe si eres sprinter o maratonista! 🏅'
    },

    'rs9939609': {
        'rsid': 'rs9939609',
        'gene': 'FTO',
        'category': 'Salud',
        'subcategory': 'Peso corporal',
        'title': 'Gen de la obesidad (FTO)',
        'description': (
            'El gen FTO (Fat Mass and Obesity Associated) regula el metabolismo energético '
            'y el control del apetito a nivel hipotalámico. '
            'El alelo A de riesgo está asociado a mayor apetito, menor sensación de saciedad '
            'y tendencia a mayor índice de masa corporal (IMC). '
            'Con dieta y ejercicio adecuados, este efecto puede minimizarse.'
        ),
        'interpretations': {
            'TT': {'result': 'Sin riesgo aumentado', 'emoji': '✅', 'detail': 'Alelo de protección. Regulación del apetito normal. Sin riesgo genético adicional de obesidad.'},
            'AT': {'result': 'Riesgo moderado', 'emoji': '⚖️', 'detail': 'Un alelo de riesgo. Ligera tendencia a mayor apetito. IMC promedio 1,5 kg/m² mayor que TT.'},
            'AA': {'result': 'Mayor tendencia a la obesidad', 'emoji': '⚠️', 'detail': 'Dos alelos de riesgo. IMC promedio 3 kg/m² mayor. El ejercicio regular puede neutralizar este efecto genético.'},
        },
        'fun_fact': 'El ejercicio físico regular puede ANULAR por completo el efecto del gen FTO. Un estudio con 200.000 personas demostró que los activos físicamente con alelo AA tenían el mismo peso que los TT sedentarios. 🏋️'
    },

    'rs12203592': {
        'rsid': 'rs12203592',
        'gene': 'IRF4',
        'category': 'Rasgo',
        'subcategory': 'Pigmentación',
        'title': 'Propensión a las pecas',
        'description': (
            'El gen IRF4 regula la expresión de varios genes de pigmentación. '
            'El alelo T en rs12203592 está fuertemente asociado a la presencia de pecas, '
            'color de cabello claro y sensibilidad al sol. '
            'Es uno de los marcadores más predictivos de pecas en europeos.'
        ),
        'interpretations': {
            'CC': {'result': 'Sin predisposición a pecas', 'emoji': '🌟', 'detail': 'Alelo C protector. Baja probabilidad de pecas. Pigmentación más uniforme.'},
            'CT': {'result': 'Moderada predisposición', 'emoji': '✨', 'detail': 'Un alelo T. Posibles pocas pecas, especialmente con exposición solar.'},
            'TT': {'result': 'Alta predisposición a pecas', 'emoji': '🌈', 'detail': 'Dos alelos T. Alta probabilidad de tener pecas. Piel muy sensible al sol. Frecuente en irlandeses y escoceses.'},
        },
        'fun_fact': 'Las pecas son depósitos focales de melanina que aumentan con el sol. En la antigüedad, algunas culturas las consideraban signos de belleza mágica o de toques del sol. ☀️'
    },

    # ────────────────────────────────────────────────────────────────
    # METABOLISMO Y NUTRICIÓN
    # ────────────────────────────────────────────────────────────────

    'rs762551': {
        'rsid': 'rs762551',
        'gene': 'CYP1A2',
        'category': 'Metabolismo',
        'subcategory': 'Cafeína',
        'title': 'Metabolismo de la cafeína (CYP1A2)',
        'description': (
            'El gen CYP1A2 codifica la enzima que metaboliza el 95% de la cafeína en el hígado. '
            'El alelo A de rs762551 está asociado a mayor inducibilidad de CYP1A2 '
            'por los alimentos (metabolizador rápido), '
            'mientras que el alelo C produce una enzima más lenta.'
        ),
        'interpretations': {
            'AA': {'result': 'Metabolizador rápido de cafeína', 'emoji': '⚡', 'detail': 'La cafeína se elimina rápido. Puedes tomar café por la tarde sin problemas de sueño. Bajo riesgo cardiovascular por cafeína.'},
            'AC': {'result': 'Metabolizador moderado', 'emoji': '☕', 'detail': 'Velocidad intermedia. La cafeína tiene efecto más prolongado. Cuidado con el café después de las 3pm.'},
            'CC': {'result': 'Metabolizador lento de cafeína', 'emoji': '🐌', 'detail': 'La cafeína se queda mucho más tiempo en el cuerpo. Mayor riesgo de insomnio y palpitaciones con alto consumo.'},
        },
        'fun_fact': 'Los metabolizadores lentos de cafeína tienen hasta 1,4 veces más riesgo cardiovascular si beben 4 o más tazas de café al día. ¡Tu genoma sabe cuánto café es demasiado! ☕'
    },

    'rs1800497': {
        'rsid': 'rs1800497',
        'gene': 'ANKK1/DRD2',
        'category': 'Metabolismo',
        'subcategory': 'Dopamina',
        'title': 'Gen del placer y la recompensa (DRD2)',
        'description': (
            'El SNP rs1800497 (Taq1A) está ubicado en el gen ANKK1, '
            'cerca del receptor de dopamina D2 (DRD2). '
            'El alelo A1 (T) se asocia a menor densidad de receptores D2, '
            'lo que puede llevar a buscar mayor estimulación para obtener la misma satisfacción. '
            'Se ha relacionado con comportamientos adictivos, búsqueda de novedades y también mayor creatividad.'
        ),
        'interpretations': {
            'CC': {'result': 'Sistema de recompensa estándar', 'emoji': '😊', 'detail': 'Alta densidad de receptores D2. Sistema de recompensa eficiente. Menor tendencia a conductas de búsqueda de estimulación.'},
            'CT': {'result': 'Moderada reducción de D2', 'emoji': '🎨', 'detail': 'Menor densidad de receptores. Posible búsqueda de mayor estimulación. Frecuente asociación con personalidades creativas.'},
            'TT': {'result': 'Baja densidad de receptores D2', 'emoji': '🎲', 'detail': 'Reducción notable en receptores D2. Mayor propensión a buscar experiencias intensas. Importantes precauciones con sustancias.'},
        },
        'fun_fact': 'Este gen ha sido llamado el "gen del aburrimiento". Las personas con el alelo A1 pueden procesar el placer de forma diferente y necesitar estímulos más intensos. 🎡'
    },

    'rs4244285': {
        'rsid': 'rs4244285',
        'gene': 'CYP2C19',
        'category': 'Metabolismo',
        'subcategory': 'Medicamentos',
        'title': 'Metabolismo de medicamentos (CYP2C19)',
        'description': (
            'El gen CYP2C19 codifica una enzima hepática que metaboliza muchos medicamentos: '
            'antiácidos (omeprazol), anticoagulantes (clopidogrel), antidepresivos y antiepilépticos. '
            'La variante A en rs4244285 es la mutación *2 (pérdida de función). '
            'Los portadores AA son metabolizadores pobres: los medicamentos se acumulan más.'
        ),
        'interpretations': {
            'GG': {'result': 'Metabolizador normal', 'emoji': '💊', 'detail': 'CYP2C19 funcional. Las dosis estándar de medicamentos funcionan como se espera.'},
            'AG': {'result': 'Metabolizador intermedio', 'emoji': '⚗️', 'detail': 'Un alelo con reducción parcial. Algunos medicamentos pueden necesitar ajuste de dosis.'},
            'AA': {'result': 'Metabolizador pobre', 'emoji': '⚠️', 'detail': 'Sin función CYP2C19. El omeprazol puede ser más eficaz; el clopidogrel menos activo. Consultar médico para ajuste.'},
        },
        'fun_fact': 'El 15-20% de los asiáticos son metabolizadores pobres de CYP2C19, frente al 2-5% en europeos. Esta diferencia explica por qué las mismas dosis no funcionan igual en todas las poblaciones. 🧬'
    },

    'rs1801133': {
        'rsid': 'rs1801133',
        'gene': 'MTHFR',
        'category': 'Metabolismo',
        'subcategory': 'Folato y vitaminas',
        'title': 'Metabolismo del folato (MTHFR C677T)',
        'description': (
            'El gen MTHFR codifica la metilenotetrahidrofolato reductasa, '
            'enzima esencial para convertir folato en su forma activa (5-MTHF), '
            'necesaria para la síntesis de DNA, reparación celular y metabolismo de la homocisteína. '
            'La variante T reduce la eficiencia de la enzima hasta un 70%, '
            'pudiendo aumentar los niveles de homocisteína en sangre.'
        ),
        'interpretations': {
            'CC': {'result': 'Metabolismo MTHFR normal', 'emoji': '✅', 'detail': 'Enzima MTHFR totalmente funcional. Metabolismo del folato óptimo.'},
            'CT': {'result': 'Reducción moderada MTHFR', 'emoji': '🥦', 'detail': 'Actividad reducida ~30-40%. Considera aumentar el consumo de folato natural o suplementar con metilfolato.'},
            'TT': {'result': 'Reducción severa MTHFR', 'emoji': '💊', 'detail': 'Actividad reducida ~60-70%. Riesgo de homocisteína elevada. Recomienda suplementación con metilfolato (no ácido fólico sintético).'},
        },
        'fun_fact': '¡Hasta el 40% de la población tiene al menos un alelo T! El MTHFR es uno de los polimorfismos más comunes en humanos y afecta cómo procesas las verduras de hoja verde. 🌿'
    },

    'rs1800562': {
        'rsid': 'rs1800562',
        'gene': 'HFE',
        'category': 'Salud',
        'subcategory': 'Metabolismo del hierro',
        'title': 'Hemocromatosis hereditaria (HFE C282Y)',
        'description': (
            'El gen HFE regula la absorción intestinal de hierro. '
            'La mutación C282Y (rs1800562, alelo A) causa hemocromatosis hereditaria: '
            'absorción excesiva de hierro que se acumula en órganos. '
            'Es la enfermedad genética más común en europeos del norte. '
            'Con diagnóstico temprano es tratable con flebotomías regulares.'
        ),
        'interpretations': {
            'GG': {'result': 'Sin mutación C282Y', 'emoji': '✅', 'detail': 'Sin la mutación causante de hemocromatosis tipo 1. Metabolismo del hierro normal.'},
            'AG': {'result': 'Portador C282Y', 'emoji': '⚠️', 'detail': 'Portador de un alelo. Riesgo bajo de hemocromatosis, pero puede tener hierro ligeramente elevado. Monitoreo preventivo recomendado.'},
            'AA': {'result': 'Homocigoto C282Y', 'emoji': '🔴', 'detail': 'Alto riesgo de hemocromatosis hereditaria. Importante consultar médico para análisis de hierro y ferritina. Muy tratable si se detecta temprano.'},
        },
        'fun_fact': '1 de cada 200 personas de origen noreuropeo tiene hemocromatosis. La "sangría" (flebotomía) es el tratamiento, ¡igual que en la medicina medieval! 🏺'
    },

    'rs53576': {
        'rsid': 'rs53576',
        'gene': 'OXTR',
        'category': 'Rasgo',
        'subcategory': 'Comportamiento social',
        'title': 'Empatía y oxitocina (OXTR)',
        'description': (
            'El gen OXTR codifica el receptor de oxitocina, la "hormona del amor y la conexión social". '
            'La variante G en rs53576 está asociada a mayor sensibilidad al receptor de oxitocina, '
            'mayor empatía, más conductas prosociales y mejor regulación del estrés. '
            'El alelo A se asocia a menor empatía perceptiva y mayor reactividad al estrés.'
        ),
        'interpretations': {
            'GG': {'result': 'Alta empatía y conexión social', 'emoji': '💖', 'detail': 'Portador GG. Mayor sensibilidad a la oxitocina. Tendencia a ser más empático, optimista y socialmente sensible.'},
            'AG': {'result': 'Empatía moderada', 'emoji': '💙', 'detail': 'Un alelo G. Empatía normal con algunas características del genotipo G.'},
            'AA': {'result': 'Menor reactividad a la oxitocina', 'emoji': '🤝', 'detail': 'Alelo AA. Menor sensibilidad al receptor. Más independencia emocional, pero puede ser menos perceptivo en situaciones sociales.'},
        },
        'fun_fact': 'El abrazo de 20 segundos libera suficiente oxitocina para reducir el cortisol (estrés) significativamente. ¡Tu receptor OXTR determina cuánto te beneficias de los abrazos! 🤗'
    },

    'rs4680': {
        'rsid': 'rs4680',
        'gene': 'COMT',
        'category': 'Metabolismo',
        'subcategory': 'Neurotransmisores',
        'title': 'Gen guerrero vs. preocupón (COMT)',
        'description': (
            'La catecol-O-metiltransferasa (COMT) degrada la dopamina y noradrenalina en la corteza prefrontal. '
            'El alelo Val (G) produce una enzima 3-4 veces más activa que Met (A), '
            'limpiando los neurotransmisores más rápido. '
            '"Guerreros" (Val) rinden mejor bajo estrés agudo. '
            '"Preocupones" (Met) tienen mejor cognición en calma pero más ansiedad bajo presión.'
        ),
        'interpretations': {
            'GG': {'result': 'Guerrero (Warrior)', 'emoji': '⚔️', 'detail': 'Val/Val. Dopamina se limpia rápido. Mejor rendimiento bajo presión. Menos rumiación, más acción. Menor riesgo de ansiedad.'},
            'AG': {'result': 'Equilibrio guerrero-preocupón', 'emoji': '⚖️', 'detail': 'Val/Met. Combinación balanceada. Buenos bajo estrés moderado. Cierta tendencia a reflexionar.'},
            'AA': {'result': 'Preocupón (Worrier)', 'emoji': '🧐', 'detail': 'Met/Met. Dopamina elevada en prefrontal. Excelente cognición en calma, mayor creatividad. Más ansiedad bajo estrés agudo.'},
        },
        'fun_fact': '¡El gen "guerrero vs. preocupón" es real! Los Met/Met tienden a sacar mejores notas en calma pero se bloquean en exámenes estresantes. Los Val/Val hacen lo contrario. 📚'
    },

    'rs25531': {
        'rsid': 'rs25531',
        'gene': 'SLC6A4',
        'category': 'Metabolismo',
        'subcategory': 'Serotonina',
        'title': 'Transportador de serotonina (5-HTTLPR)',
        'description': (
            'El gen SLC6A4 codifica el transportador de serotonina (SERT), '
            'que recapta la serotonina de la sinapsis. '
            'rs25531 es un marcador del polimorfismo 5-HTTLPR (alelos L y S). '
            'El alelo A (alelo L con menor actividad) se asocia a mayor sensibilidad emocional '
            'y a ambientes tanto positivos como negativos.'
        ),
        'interpretations': {
            'AA': {'result': 'Alta sensibilidad emocional', 'emoji': '🎭', 'detail': 'Alelo A/A. Mayor reactividad emocional. Las experiencias positivas y negativas tienen más impacto. Mayor creatividad artística asociada.'},
            'AG': {'result': 'Sensibilidad moderada', 'emoji': '🌊', 'detail': 'Combinación de alelos. Respuesta emocional equilibrada.'},
            'GG': {'result': 'Regulación emocional estable', 'emoji': '🏔️', 'detail': 'Alelo G/G. Mayor resiliencia ante el estrés. Menor impacto de los eventos negativos. Buena regulación emocional.'},
        },
        'fun_fact': 'El alelo S del 5-HTTLPR es el "alelo de la orquídea": los portadores florecen con un entorno óptimo pero se marchitan con uno adverso. Los GG son "dientes de león": prosperan en cualquier entorno. 🌺'
    },

    'rs1800955': {
        'rsid': 'rs1800955',
        'gene': 'DRD4',
        'category': 'Rasgo',
        'subcategory': 'Personalidad',
        'title': 'Búsqueda de novedad (DRD4)',
        'description': (
            'El gen DRD4 codifica el receptor de dopamina D4. '
            'La variante T en rs1800955 se asocia a mayor búsqueda de novedad, '
            'mayor impulsividad y tendencia a la exploración. '
            'Ha sido relacionada con el gen del "nomadismo" y las migraciones humanas antiguas.'
        ),
        'interpretations': {
            'CC': {'result': 'Baja búsqueda de novedad', 'emoji': '🏠', 'detail': 'Receptor DRD4 estándar. Preferencia por la rutina y la estabilidad. Mayor facilidad para mantener hábitos.'},
            'CT': {'result': 'Búsqueda de novedad moderada', 'emoji': '🗺️', 'detail': 'Combinación de alelos. Equilibrio entre exploración y estabilidad.'},
            'TT': {'result': 'Alta búsqueda de novedad', 'emoji': '🚀', 'detail': 'Alelo T/T. Alta búsqueda de experiencias nuevas. Impulsividad, creatividad y tendencia a la exploración. Posible dificultad con rutinas.'},
        },
        'fun_fact': 'Las poblaciones que migran largas distancias tienen mayor frecuencia del alelo T. ¡Tu gen DRD4 puede revelar si tienes espíritu aventurero heredado de tus antepasados nómadas! 🌍'
    },

    'rs1800629': {
        'rsid': 'rs1800629',
        'gene': 'TNF',
        'category': 'Salud',
        'subcategory': 'Inflamación',
        'title': 'Respuesta inflamatoria (TNF-alfa)',
        'description': (
            'El gen TNF codifica el Factor de Necrosis Tumoral alfa (TNF-α), '
            'una citoquina pro-inflamatoria clave del sistema inmune. '
            'La variante A en rs1800629 aumenta la producción de TNF-α, '
            'lo que puede ser beneficioso para combatir infecciones '
            'pero también aumentar el riesgo de enfermedades inflamatorias crónicas.'
        ),
        'interpretations': {
            'GG': {'result': 'Respuesta inflamatoria estándar', 'emoji': '🛡️', 'detail': 'Producción normal de TNF-α. Respuesta inmune equilibrada.'},
            'AG': {'result': 'Mayor producción de TNF-α', 'emoji': '🔥', 'detail': 'Un alelo A. Respuesta inflamatoria algo elevada. Posiblemente más reactivo a infecciones.'},
            'AA': {'result': 'Alta producción de TNF-α', 'emoji': '⚠️', 'detail': 'Dos alelos A. Mayor producción de TNF-α. Respuesta inmune potente. Mayor riesgo de condiciones autoinmunes o inflamatorias.'},
        },
        'fun_fact': 'El TNF-α es una de las moléculas que hace que tengas fiebre cuando estás enfermo. ¡Es tu cuerpo "subiendo la temperatura" para matar bacterias y virus! 🤒'
    },

    'rs1800795': {
        'rsid': 'rs1800795',
        'gene': 'IL6',
        'category': 'Salud',
        'subcategory': 'Inflamación',
        'title': 'Interleucina 6 e inflamación (IL-6)',
        'description': (
            'La interleucina-6 (IL-6) es una citoquina multifuncional que regula la inflamación, '
            'el sistema inmune y la respuesta de fase aguda. '
            'La variante C en rs1800795 está asociada a mayor producción de IL-6, '
            'lo que puede influir en la respuesta a enfermedades inflamatorias, '
            'pero también en la adaptación al ejercicio físico.'
        ),
        'interpretations': {
            'GG': {'result': 'Baja producción basal de IL-6', 'emoji': '🌿', 'detail': 'Producción basal de IL-6 reducida. Menor tendencia a la inflamación crónica de bajo grado.'},
            'CG': {'result': 'Producción moderada de IL-6', 'emoji': '⚖️', 'detail': 'Niveles intermedios. Respuesta inflamatoria equilibrada.'},
            'CC': {'result': 'Alta producción de IL-6', 'emoji': '🔬', 'detail': 'Mayor producción de IL-6. Respuesta inmune más activa. Los deportistas CC pueden tener mejor adaptación muscular al ejercicio.'},
        },
        'fun_fact': 'La IL-6 liberada durante el ejercicio físico actúa como "mioquina" anti-inflamatoria, ¡exactamente lo contrario de cuando la produce el tejido graso! El ejercicio cambia su función. 💪'
    },

    'rs2234693': {
        'rsid': 'rs2234693',
        'gene': 'ESR1',
        'category': 'Salud',
        'subcategory': 'Hormonas',
        'title': 'Receptor de estrógeno (ESR1)',
        'description': (
            'El gen ESR1 codifica el receptor alfa de estrógenos, '
            'fundamental para la respuesta hormonal en ambos sexos. '
            'Este polimorfismo en el intrón 1 de ESR1 afecta la expresión del receptor '
            'y ha sido asociado con densidad ósea, riesgo cardiovascular '
            'y respuesta a la terapia hormonal.'
        ),
        'interpretations': {
            'TT': {'result': 'Alta expresión de receptor estrogénico', 'emoji': '🦴', 'detail': 'Mayor expresión de ESR1. Mejor respuesta a estrógenos. Posible mayor densidad ósea.'},
            'CT': {'result': 'Expresión moderada', 'emoji': '⚖️', 'detail': 'Expresión intermedia del receptor. Respuesta hormonal típica.'},
            'CC': {'result': 'Menor expresión de receptor estrogénico', 'emoji': '💡', 'detail': 'Menor expresión de ESR1. Respuesta diferente a estrógenos. Importancia en menopausia y terapia hormonal.'},
        },
        'fun_fact': 'Los estrógenos no solo son "hormonas femeninas": son fundamentales para la salud ósea, cardiovascular y cognitiva en ambos sexos. ¡Los hombres también las necesitan! 🧬'
    },

    'rs1695': {
        'rsid': 'rs1695',
        'gene': 'GSTP1',
        'category': 'Metabolismo',
        'subcategory': 'Detoxificación',
        'title': 'Detoxificación celular (GSTP1)',
        'description': (
            'El gen GSTP1 codifica la glutatión S-transferasa Pi, '
            'una enzima de fase II de detoxificación que conjuga toxinas ambientales '
            'con glutatión para su eliminación. '
            'La variante G (Ile105Val) reduce la actividad enzimática, '
            'pudiendo disminuir la capacidad de eliminar ciertos carcinógenos.'
        ),
        'interpretations': {
            'AA': {'result': 'Detoxificación GSTP1 eficiente', 'emoji': '🌿', 'detail': 'Enzima GSTP1 de alta actividad. Buena capacidad de eliminar toxinas ambientales.'},
            'AG': {'result': 'Detoxificación moderada', 'emoji': '🍃', 'detail': 'Actividad enzimática intermedia. Capacidad de detoxificación normal.'},
            'GG': {'result': 'Menor actividad GSTP1', 'emoji': '🔬', 'detail': 'Enzima con menor eficiencia. Posible menor capacidad de eliminar ciertas toxinas. Importante evitar exposición a carcinógenos ambientales.'},
        },
        'fun_fact': 'El brócoli y las crucíferas contienen sulforafano, que ACTIVA los genes de detoxificación como GSTP1. ¡Comer brócoli puede compensar tener un GSTP1 menos eficiente! 🥦'
    },

    # ────────────────────────────────────────────────────────────────
    # SALUD
    # ────────────────────────────────────────────────────────────────

    'rs429358': {
        'rsid': 'rs429358',
        'gene': 'APOE',
        'category': 'Salud',
        'subcategory': 'Riesgo cardiovascular y cognitivo',
        'title': 'Gen APOE (riesgo educativo)',
        'description': (
            'El gen APOE codifica la apolipoproteína E, importante para el transporte de colesterol. '
            'Junto con rs7412, determina el haplotipo APOE (ε2, ε3, ε4). '
            'El haplotipo ε4 (C en rs429358) se asocia a mayor riesgo de colesterol elevado y '
            'ha sido asociado epidemiológicamente con factores de riesgo cognitivo en edades avanzadas. '
            'Esta información es solo educativa y no es diagnóstica.'
        ),
        'interpretations': {
            'TT': {'result': 'Sin alelo ε4 (rs429358)', 'emoji': '✅', 'detail': 'Ausencia del alelo ε4 en este marcador. Favorable para perfil lipídico. Ver rs7412 para haplotipo completo.'},
            'CT': {'result': 'Portador de un ε4 (rs429358)', 'emoji': '💛', 'detail': 'Un alelo C. Información educativa: considerar estilo de vida saludable, ejercicio y dieta mediterránea.'},
            'CC': {'result': 'Dos alelos ε4 (rs429358)', 'emoji': '📚', 'detail': 'Solo informativo. El estilo de vida saludable (ejercicio, sueño, dieta) es el factor modificable más importante independientemente del genotipo.'},
        },
        'fun_fact': 'El APOE ε4 fue probablemente adaptativo en entornos ancestrales con alta carga parasitaria. ¡Lo que hoy puede ser un riesgo, fue una ventaja en la prehistoria! 🦠'
    },

    'rs7412': {
        'rsid': 'rs7412',
        'gene': 'APOE',
        'category': 'Salud',
        'subcategory': 'Perfil lipídico',
        'title': 'APOE haplotipo complementario',
        'description': (
            'Junto con rs429358, este SNP define el haplotipo APOE. '
            'El alelo T en rs7412 con T en rs429358 corresponde al haplotipo ε2 '
            '(asociado a colesterol más bajo y longevidad). '
            'Esta información es solo educativa y orientativa.'
        ),
        'interpretations': {
            'CC': {'result': 'Alelo C en rs7412', 'emoji': '🔬', 'detail': 'Sin el alelo ε2. Hay que combinar con rs429358 para haplotipo completo.'},
            'CT': {'result': 'Portador de alelo T en rs7412', 'emoji': '💙', 'detail': 'Un alelo T. Puede contribuir al haplotipo ε2 (longevidad favorable).'},
            'TT': {'result': 'Homocigoto T en rs7412', 'emoji': '🌟', 'detail': 'Dos alelos T. Asociado con perfil lipídico favorable y posiblemente haplotipo ε2/ε2.'},
        },
        'fun_fact': 'Los centenarios del mundo (superan los 100 años) tienen mayor frecuencia del haplotipo APOE ε2. ¡El gen de la longevidad está relacionado con el colesterol! 🎂'
    },

    'rs1801131': {
        'rsid': 'rs1801131',
        'gene': 'MTHFR',
        'category': 'Metabolismo',
        'subcategory': 'Folato y vitaminas',
        'title': 'MTHFR A1298C (variante secundaria)',
        'description': (
            'Segunda variante importante del gen MTHFR. '
            'La mutación A1298C (rs1801131, alelo C) también reduce la actividad de MTHFR, '
            'aunque en menor grado que C677T (rs1801133). '
            'Tener ambas mutaciones en heterocigosis puede tener un efecto combinado significativo.'
        ),
        'interpretations': {
            'AA': {'result': 'Sin variante A1298C', 'emoji': '✅', 'detail': 'MTHFR A1298C sin mutación. Función enzimática normal en este locus.'},
            'AC': {'result': 'Portador A1298C', 'emoji': '🔶', 'detail': 'Un alelo C. Leve reducción de actividad MTHFR. Especialmente relevante si también tienes C677T.'},
            'CC': {'result': 'Homocigoto A1298C', 'emoji': '⚠️', 'detail': 'Reducción moderada de MTHFR. Considera suplementación con metilfolato activo.'},
        },
        'fun_fact': 'MTHFR convierte el ácido fólico de los alimentos en la forma que puede usar el cerebro. ¡Es literalmente el gen que te ayuda a aprovechar las verduras! 🥬'
    },

    'rs334': {
        'rsid': 'rs334',
        'gene': 'HBB',
        'category': 'Salud',
        'subcategory': 'Hemoglobina',
        'title': 'Anemia falciforme (HBB E6V)',
        'description': (
            'El gen HBB codifica la cadena beta de la hemoglobina. '
            'La mutación E6V (rs334, alelo T) causa la sustitución Glu→Val en la posición 6, '
            'produciendo hemoglobina S que puede polimerizar con oxígeno bajo, '
            'causando anemia falciforme en homocigotos. '
            'Los portadores heterocigotos (AS) están protegidos contra la malaria grave.'
        ),
        'interpretations': {
            'AA': {'result': 'Hemoglobina AA normal', 'emoji': '❤️', 'detail': 'Sin mutación HbS. Hemoglobina completamente normal.'},
            'AT': {'result': 'Portador HbS (rasgo falciforme)', 'emoji': '🟠', 'detail': 'Portador AS. Generalmente sano. Protección parcial contra malaria grave. Raramente síntomas en condiciones extremas.'},
            'TT': {'result': 'Anemia falciforme HbSS', 'emoji': '🔴', 'detail': 'Diagnóstico de anemia falciforme. Requiere seguimiento médico especializado. Hay tratamientos efectivos disponibles.'},
        },
        'fun_fact': 'La anemia falciforme es un ejemplo perfecto de evolución: el alelo T fue seleccionado en África subsahariana porque protege a los portadores contra la malaria, la mayor causa de muerte histórica. 🦟'
    },

    # ────────────────────────────────────────────────────────────────
    # ANCESTRÍA
    # ────────────────────────────────────────────────────────────────

    'rs3827760': {
        'rsid': 'rs3827760',
        'gene': 'EDAR',
        'category': 'Ancestría',
        'subcategory': 'Este asiático',
        'title': 'Rasgos del Este Asiático (EDARV370A)',
        'description': (
            'El gen EDAR regula el desarrollo de pelo, dientes, glándulas sudoríparas y piel. '
            'La variante A (EDARV370A) surgió en China hace ~30.000 años y se extendió '
            'por toda Asia Oriental y las Américas. '
            'Esta variante produce: cabello más grueso y oscuro, mayor número de glándulas sudoríparas, '
            'incisivos en forma de pala y pechos más densos en mujeres.'
        ),
        'interpretations': {
            'GG': {'result': 'Sin variante EDARV370A', 'emoji': '🌍', 'detail': 'Alelo ancestral. Sin los rasgos específicos del este asiático. Típico en europeos y africanos.'},
            'AG': {'result': 'Portador de EDARV370A', 'emoji': '🌏', 'detail': 'Un alelo A. Mezcla de poblaciones. Posibles rasgos intermedios de cabello y glándulas.'},
            'AA': {'result': 'EDARV370A homocigoto', 'emoji': '🎏', 'detail': 'Dos alelos A. Típico de poblaciones del este asiático y americanas indígenas. Cabello grueso y oscuro, más glándulas sudoríparas.'},
        },
        'fun_fact': 'EDARV370A es una de las selecciones positivas más fuertes en humanos recientes. Incluso cambia la forma de los dientes: los asiáticos tienen incisivos "en pala" por este gen. 😁'
    },

    'rs1426654': {
        'rsid': 'rs1426654',
        'gene': 'SLC24A5',
        'category': 'Ancestría',
        'subcategory': 'Pigmentación europeo-africana',
        'title': 'Marcador de pigmentación europeo (SLC24A5)',
        'description': (
            'El gen SLC24A5 es uno de los principales determinantes del color de piel entre europeos y africanos/sur-asiáticos. '
            'El alelo A (Ala111Thr) explica hasta el 35-38% de la diferencia de pigmentación '
            'entre europeos y africanos. '
            'El alelo A surgió en el Medio Oriente hace ~6.000-10.000 años y se difundió en Europa.'
        ),
        'interpretations': {
            'AA': {'result': 'Ascendencia europea/sur-asiática', 'emoji': '🏔️', 'detail': 'Homocigoto A. Marcador muy frecuente en europeos y sur-asiáticos. Asociado a piel más clara.'},
            'AG': {'result': 'Ancestría mixta', 'emoji': '🌐', 'detail': 'Heterocigoto. Mezcla de linajes. Frecuente en poblaciones admixtas.'},
            'GG': {'result': 'Alelo ancestral africano', 'emoji': '🌍', 'detail': 'Alelo G ancestral. Muy frecuente en africanos subsaharianos y algunos grupos de Asia Oriental.'},
        },
        'fun_fact': '¡Un solo gen explica el 38% de la diferencia de color de piel entre europeos y africanos! SLC24A5 es el SNP individual más influyente en pigmentación humana conocido. 🎨'
    },

    'rs16891982': {
        'rsid': 'rs16891982',
        'gene': 'SLC45A2',
        'category': 'Ancestría',
        'subcategory': 'Pigmentación europea',
        'title': 'Pigmentación europea (SLC45A2)',
        'description': (
            'El gen SLC45A2 (también conocido como MATP) regula el transporte en los melanosomas. '
            'El alelo C (rs16891982) es casi exclusivo de europeos y está asociado a piel clara, '
            'ojos claros y cabello rubio o castaño claro. '
            'Es uno de los marcadores más discriminantes de ascendencia europea.'
        ),
        'interpretations': {
            'GG': {'result': 'Alelo ancestral no europeo', 'emoji': '🌍', 'detail': 'Alelo G. Frecuente en africanos, asiáticos y amerindios. Asociado a pigmentación más oscura.'},
            'CG': {'result': 'Mezcla de ascendencia', 'emoji': '🌐', 'detail': 'Heterocigoto. Indica mezcla de linajes europeo y no europeo.'},
            'CC': {'result': 'Marcador europeo', 'emoji': '🏰', 'detail': 'Homocigoto C. Casi exclusivo de europeos. Muy asociado a piel clara, ojos y cabello claros.'},
        },
        'fun_fact': 'El hombre de Cheddar (Cheddar Man), el europeo de 10.000 años cuyo genoma fue secuenciado en 2018, tenía piel muy oscura. ¡La piel clara en Europa es relativamente reciente! 🦴'
    },

    'rs2814778': {
        'rsid': 'rs2814778',
        'gene': 'DARC/ACKR1',
        'category': 'Ancestría',
        'subcategory': 'Africano',
        'title': 'Antígeno Duffy y protección contra malaria (DARC)',
        'description': (
            'El gen DARC codifica el antígeno Duffy, un receptor en glóbulos rojos. '
            'El alelo C (rs2814778) en africanos subsaharianos elimina la expresión de DARC '
            'en eritrocitos, proporcionando resistencia total contra Plasmodium vivax, '
            'un parásito de la malaria. '
            'Es prácticamente universal en África subsahariana.'
        ),
        'interpretations': {
            'TT': {'result': 'Duffy positivo', 'emoji': '🔬', 'detail': 'Expresa el antígeno Duffy. Susceptible a P. vivax. Ascendencia no subsahariana típicamente.'},
            'CT': {'result': 'Portador mixto Duffy', 'emoji': '🌐', 'detail': 'Un alelo C. Mezcla de ancestría africana y no africana. Expresión reducida de Duffy en eritrocitos.'},
            'CC': {'result': 'Duffy negativo', 'emoji': '🛡️', 'detail': 'Sin antígeno Duffy en eritrocitos. Resistencia natural a P. vivax. Marcador de ancestría africana subsahariana.'},
        },
        'fun_fact': 'El 100% de los africanos de algunas regiones de África Occidental son Duffy negativos. ¡Esta mutación salvó a millones de personas de la malaria a lo largo de miles de años! 🦟'
    },

    'rs4833103': {
        'rsid': 'rs4833103',
        'gene': 'TNFRSF8',
        'category': 'Ancestría',
        'subcategory': 'Herencia neandertal',
        'title': 'Variante neandertal (TNFRSF8)',
        'description': (
            'Este SNP ha sido identificado como un marcador de introgresión de ADN neandertal '
            'en el genoma humano moderno. '
            'Aproximadamente el 1-4% del genoma de los europeos y asiáticos proviene de neandertales. '
            'Este marcador específico puede indicar variantes heredadas de nuestros primos extintos.'
        ),
        'interpretations': {
            'AA': {'result': 'Sin variante neandertal detectada', 'emoji': '🦴', 'detail': 'Sin este marcador de introgresión neandertal en TNFRSF8.'},
            'AC': {'result': 'Portador de variante neandertal', 'emoji': '🗿', 'detail': 'Portador heterocigoto de este marcador. Posible herencia de ADN neandertal en esta región.'},
            'CC': {'result': 'Variante neandertal presente', 'emoji': '🏔️', 'detail': 'Homocigoto para el marcador de introgresión neandertal. Herencia de variante antigua en esta región genómica.'},
        },
        'fun_fact': '¡Los humanos modernos y los neandertales se mezclaron! Hasta el 4% de tu ADN puede ser neandertal. Los neandertales nos dieron genes de inmunidad, adaptación al frío y posiblemente el pelo oscuro. 🧊'
    },

    # ────────────────────────────────────────────────────────────────
    # RASGOS Y METABOLISMO ADICIONALES
    # ────────────────────────────────────────────────────────────────

    'rs1051730': {
        'rsid': 'rs1051730',
        'gene': 'CHRNA3',
        'category': 'Salud',
        'subcategory': 'Dependencia al tabaco',
        'title': 'Dependencia a la nicotina (CHRNA3)',
        'description': (
            'El gen CHRNA3 codifica una subunidad del receptor nicotínico de acetilcolina. '
            'La variante T se asocia a mayor dependencia a la nicotina, '
            'mayor número de cigarrillos al día entre fumadores '
            'y mayor dificultad para dejar de fumar.'
        ),
        'interpretations': {
            'CC': {'result': 'Menor dependencia a nicotina', 'emoji': '✅', 'detail': 'Sin el alelo de riesgo. Menor tendencia a la dependencia de la nicotina si se fuma.'},
            'CT': {'result': 'Dependencia moderada', 'emoji': '⚠️', 'detail': 'Un alelo T. Riesgo moderado de dependencia. El apoyo para dejar de fumar es efectivo.'},
            'TT': {'result': 'Mayor dependencia a nicotina', 'emoji': '🚬', 'detail': 'Dos alelos T. Mayor tendencia a fumar más y mayor dificultad para dejar el hábito. Considerar ayuda farmacológica.'},
        },
        'fun_fact': 'Las personas con dos alelos T fuman en promedio 1 cigarrillo más por día y tienen 1,5 veces más dificultad para dejar el tabaco que los CC. 🚭'
    },

    'rs1799945': {
        'rsid': 'rs1799945',
        'gene': 'HFE',
        'category': 'Salud',
        'subcategory': 'Metabolismo del hierro',
        'title': 'Hemocromatosis HFE H63D',
        'description': (
            'Segunda variante del gen HFE asociada a hemocromatosis hereditaria. '
            'La mutación H63D (rs1799945, alelo G) es más frecuente que C282Y '
            'pero tiene menor penetrancia. '
            'Produce un leve aumento en la absorción de hierro, '
            'especialmente en combinación con la mutación C282Y (rs1800562).'
        ),
        'interpretations': {
            'CC': {'result': 'Sin mutación H63D', 'emoji': '✅', 'detail': 'Sin la variante H63D. Absorción de hierro normal en este locus.'},
            'CG': {'result': 'Portador H63D', 'emoji': '🔶', 'detail': 'Portador de un alelo G. Leve tendencia a mayor absorción de hierro. Monitoreo de ferritina recomendado.'},
            'GG': {'result': 'Homocigoto H63D', 'emoji': '⚠️', 'detail': 'Dos alelos G. Mayor riesgo de sobrecarga de hierro, especialmente combinado con C282Y. Consultar médico.'},
        },
        'fun_fact': 'La hemocromatosis fue llamada "la diabetes de bronce" porque el exceso de hierro pigmenta la piel de color bronceado. El tratamiento es simplemente donar sangre regularmente. 🩸'
    },

    'rs7903146': {
        'rsid': 'rs7903146',
        'gene': 'TCF7L2',
        'category': 'Salud',
        'subcategory': 'Diabetes tipo 2',
        'title': 'Riesgo de diabetes tipo 2 (TCF7L2)',
        'description': (
            'TCF7L2 (Factor de transcripción 7-like 2) es el gen con mayor impacto genético '
            'en el riesgo de diabetes tipo 2. '
            'Regula la secreción de insulina e incretinas en el páncreas. '
            'El alelo T de riesgo aumenta el riesgo de DM2 en ~1,4-1,5 veces por alelo.'
        ),
        'interpretations': {
            'CC': {'result': 'Sin riesgo aumentado de DM2', 'emoji': '✅', 'detail': 'Sin el alelo de riesgo de diabetes. Riesgo genético estándar.'},
            'CT': {'result': 'Riesgo moderadamente aumentado', 'emoji': '🍎', 'detail': 'Un alelo T. Riesgo ~1,4 veces mayor. Dieta mediterránea y ejercicio son preventivos efectivos.'},
            'TT': {'result': 'Riesgo aumentado de DM2', 'emoji': '🩺', 'detail': 'Dos alelos T. Mayor riesgo genético. El estilo de vida saludable reduce este riesgo de forma muy significativa.'},
        },
        'fun_fact': 'Incluso teniendo el alelo de riesgo de TCF7L2, hacer 150 minutos de ejercicio por semana reduce el riesgo de diabetes en un 58%. ¡Los genes no son destino! 🏃'
    },

    'rs1800977': {
        'rsid': 'rs1800977',
        'gene': 'KLOTHO',
        'category': 'Salud',
        'subcategory': 'Envejecimiento',
        'title': 'Gen de la longevidad (KLOTHO)',
        'description': (
            'El gen KLOTHO fue nombrado en honor a la diosa griega que hila el hilo de la vida. '
            'Regula el metabolismo del fosfato, la función renal y el envejecimiento. '
            'La variante KL-VS (rs1800977) está asociada a mayor longevidad, '
            'mejor función cognitiva y menor riesgo cardiovascular.'
        ),
        'interpretations': {
            'CC': {'result': 'Sin variante KL-VS', 'emoji': '⏰', 'detail': 'Sin el alelo de longevidad. Función KLOTHO estándar.'},
            'CT': {'result': 'Portador de variante KL-VS', 'emoji': '⌛', 'detail': 'Un alelo de variante. Posible leve aumento de longevidad y función cognitiva.'},
            'TT': {'result': 'Homocigoto KL-VS', 'emoji': '🌟', 'detail': 'Variante asociada a mayor longevidad y mejor función cognitiva en algunos estudios. ¡El gen "antiedad"!'},
        },
        'fun_fact': 'Los ratones que sobreexpresan KLOTHO viven un 30% más que los normales. En humanos, la variante KL-VS se encuentra con mayor frecuencia en centenarios. 🎂'
    },

    'rs1799752': {
        'rsid': 'rs1799752',
        'gene': 'ACE',
        'category': 'Salud',
        'subcategory': 'Sistema cardiovascular',
        'title': 'Enzima convertidora de angiotensina (ACE)',
        'description': (
            'El gen ACE (Enzima Convertidora de Angiotensina) regula la presión arterial '
            'y la función cardiovascular. '
            'El polimorfismo Inserción/Deleción (I/D) en rs1799752 afecta los niveles de ACE: '
            'el alelo D produce niveles más altos de ACE, '
            'asociados a mayor resistencia en ejercicios de fuerza '
            'pero también a mayor riesgo cardiovascular en algunos contextos.'
        ),
        'interpretations': {
            'II': {'result': 'Inserción/Inserción (baja ACE)', 'emoji': '🏃', 'detail': 'Bajos niveles de ACE. Mejor rendimiento en deportes de resistencia. Menor presión arterial en respuesta al ejercicio.'},
            'ID': {'result': 'Heterocigoto (ACE moderada)', 'emoji': '⚖️', 'detail': 'Niveles intermedios de ACE. Buen rendimiento en deportes mixtos.'},
            'DD': {'result': 'Deleción/Deleción (alta ACE)', 'emoji': '💪', 'detail': 'Altos niveles de ACE. Ventaja en deportes de fuerza y potencia. Asociado a mejor ganancia muscular.'},
        },
        'fun_fact': 'La mayoría de los montañistas que coronan el Everest sin oxígeno suplementario son genotipo II (baja ACE). ¡Tu gen de presión arterial puede influir en tus aventuras extremas! ⛰️'
    },

    'rs2187668': {
        'rsid': 'rs2187668',
        'gene': 'HLA-DQ',
        'category': 'Salud',
        'subcategory': 'Sistema inmune',
        'title': 'Riesgo de enfermedad celíaca (HLA-DQ2)',
        'description': (
            'El haplotipo HLA-DQ2 es el principal factor de riesgo genético para la enfermedad celíaca. '
            'Este SNP es un marcador proxy del haplotipo DQ2.5. '
            'Aproximadamente el 95% de los celíacos portan HLA-DQ2 o DQ8, '
            'pero solo el 2-3% de los portadores desarrollan la enfermedad.'
        ),
        'interpretations': {
            'GG': {'result': 'Sin marcador HLA-DQ2', 'emoji': '✅', 'detail': 'Sin el marcador de riesgo principal de celíaca. Riesgo muy bajo de desarrollar enfermedad celíaca.'},
            'AG': {'result': 'Portador de marcador DQ2', 'emoji': '🌾', 'detail': 'Portador heterocigoto. Riesgo aumentado pero la mayoría de portadores nunca desarrollan celíaca.'},
            'AA': {'result': 'Homocigoto marcador DQ2', 'emoji': '⚠️', 'detail': 'Mayor carga de riesgo genético de celíaca. No implica diagnóstico. Solo con síntomas y biopsia puede confirmarse.'},
        },
        'fun_fact': 'El gluten solo fue introducido en la dieta humana hace ~10.000 años con la agricultura. ¡El sistema inmune de algunos humanos todavía no se ha "acostumbrado" a esta proteína! 🌾'
    },

    'rs1800469': {
        'rsid': 'rs1800469',
        'gene': 'TGFB1',
        'category': 'Salud',
        'subcategory': 'Inflamación y reparación',
        'title': 'Factor de crecimiento TGF-beta1',
        'description': (
            'El gen TGFB1 codifica el Factor de Crecimiento Transformante Beta-1, '
            'involucrado en la regulación inmune, la cicatrización y la fibrosis. '
            'La variante C en rs1800469 está asociada a mayor producción de TGF-β1, '
            'lo que puede influir en la reparación tisular y la respuesta inflamatoria.'
        ),
        'interpretations': {
            'TT': {'result': 'Producción normal de TGF-β1', 'emoji': '🌿', 'detail': 'Niveles estándar de TGF-β1. Respuesta inflamatoria y reparadora normal.'},
            'CT': {'result': 'Producción moderada elevada', 'emoji': '🔧', 'detail': 'Un alelo C. Ligero aumento en la producción de TGF-β1.'},
            'CC': {'result': 'Alta producción de TGF-β1', 'emoji': '🏥', 'detail': 'Niveles elevados de TGF-β1. Mejor cicatrización, pero mayor riesgo de fibrosis en órganos bajo estrés crónico.'},
        },
        'fun_fact': 'El TGF-β1 es tan potente que se usa en investigación para regenerar hueso y cartílago. También es el principal responsable de que las cicatrices se endurezcan con el tiempo. 🔬'
    },

    'rs2066845': {
        'rsid': 'rs2066845',
        'gene': 'NOD2',
        'category': 'Salud',
        'subcategory': 'Sistema inmune',
        'title': 'Inmunidad innata y enfermedad de Crohn (NOD2)',
        'description': (
            'El gen NOD2 codifica un receptor intracelular del sistema inmune innato '
            'que reconoce bacterias. '
            'La variante G (rs2066845) altera la función de NOD2 y ha sido asociada '
            'con mayor riesgo de enfermedad de Crohn y otras enfermedades inflamatorias intestinales. '
            'Información educativa solamente.'
        ),
        'interpretations': {
            'CC': {'result': 'NOD2 funcional normal', 'emoji': '✅', 'detail': 'Función inmune innata intestinal normal en este locus.'},
            'CG': {'result': 'Portador de variante NOD2', 'emoji': '⚠️', 'detail': 'Portador de un alelo G. Riesgo ligeramente aumentado de enfermedad inflamatoria intestinal.'},
            'GG': {'result': 'Variante NOD2 homocigota', 'emoji': '🩺', 'detail': 'Mayor alteración en la función de NOD2. Riesgo aumentado de enfermedad de Crohn. Consultar gastroenterólogo si hay síntomas.'},
        },
        'fun_fact': 'La enfermedad de Crohn aumentó drásticamente con la urbanización y los antibióticos. El microbioma intestinal puede modular el efecto del gen NOD2. ¡Tu flora intestinal es su propio genoma! 🦠'
    },

    'rs9930506': {
        'rsid': 'rs9930506',
        'gene': 'FTO',
        'category': 'Salud',
        'subcategory': 'Peso corporal',
        'title': 'Regulación del apetito (FTO - rs9930506)',
        'description': (
            'Segunda variante importante en el gen FTO relacionada con el IMC y el apetito. '
            'Actúa en la misma región regulatoria que rs9939609. '
            'El alelo G está asociado a mayor consumo calórico e IMC más elevado.'
        ),
        'interpretations': {
            'AA': {'result': 'Sin riesgo adicional FTO', 'emoji': '✅', 'detail': 'Alelo A. Sin el segundo marcador de riesgo de obesidad en FTO.'},
            'AG': {'result': 'Riesgo moderado FTO', 'emoji': '⚖️', 'detail': 'Un alelo G. Ligero aumento en tendencia al sobrepeso.'},
            'GG': {'result': 'Riesgo aumentado FTO', 'emoji': '⚠️', 'detail': 'Dos alelos G. Mayor tendencia al sobrepeso. El ejercicio cardiovascular regular tiene efecto compensatorio demostrado.'},
        },
        'fun_fact': 'FTO significa "Fat mass and Obesity associated" pero fue descubierto originalmente estudiando diabetes tipo 2. ¡El descubrimiento del gen de la obesidad fue un accidente científico! 🔬'
    },

    'rs1800588': {
        'rsid': 'rs1800588',
        'gene': 'LIPC',
        'category': 'Salud',
        'subcategory': 'Colesterol',
        'title': 'Colesterol HDL (lipasa hepática)',
        'description': (
            'El gen LIPC codifica la lipasa hepática, que degrada el HDL (colesterol bueno). '
            'La variante T en rs1800588 reduce la actividad de la lipasa hepática, '
            'resultando en niveles más altos de HDL. '
            'Un HDL elevado es generalmente cardioprotector.'
        ),
        'interpretations': {
            'CC': {'result': 'Lipasa hepática normal', 'emoji': '💙', 'detail': 'Actividad normal de la lipasa hepática. HDL en rango estándar.'},
            'CT': {'result': 'Lipasa moderadamente reducida', 'emoji': '💚', 'detail': 'Un alelo T. Ligero aumento en HDL. Beneficioso para salud cardiovascular.'},
            'TT': {'result': 'HDL elevado', 'emoji': '💛', 'detail': 'Dos alelos T. Lipasa hepática reducida. Niveles de HDL más altos. Factor cardioprotector.'},
        },
        'fun_fact': 'El HDL es el "camión de basura" del colesterol: recoge el colesterol de las arterias y lo lleva al hígado para eliminarlo. ¡Más HDL significa arterias más limpias! 🚛'
    },

    'rs2070895': {
        'rsid': 'rs2070895',
        'gene': 'LIPC',
        'category': 'Salud',
        'subcategory': 'Colesterol',
        'title': 'Colesterol HDL - segunda variante',
        'description': (
            'Segunda variante en el gen LIPC que también influye en los niveles de HDL. '
            'El alelo A se asocia a mayor actividad de lipasa hepática '
            'y menor HDL, mientras que el G está asociado a HDL más elevado.'
        ),
        'interpretations': {
            'AA': {'result': 'Mayor actividad lipasa', 'emoji': '⚖️', 'detail': 'Niveles de HDL pueden ser más bajos. Importante mantener dieta saludable y ejercicio.'},
            'AG': {'result': 'Actividad lipasa intermedia', 'emoji': '💚', 'detail': 'HDL en rango intermedio. Buen equilibrio.'},
            'GG': {'result': 'Menor actividad lipasa', 'emoji': '💛', 'detail': 'HDL potencialmente más elevado. Factor cardioprotector positivo.'},
        },
        'fun_fact': 'El aguacate y el aceite de oliva son de los alimentos que más aumentan el HDL. ¡La dieta mediterránea es la más respaldada científicamente para optimizar el colesterol! 🥑'
    },

    'rs2108622': {
        'rsid': 'rs2108622',
        'gene': 'CYP4F2',
        'category': 'Metabolismo',
        'subcategory': 'Medicamentos',
        'title': 'Metabolismo de la vitamina K y warfarina (CYP4F2)',
        'description': (
            'El gen CYP4F2 metaboliza la vitamina K en el hígado. '
            'La variante T (rs2108622) reduce la actividad de CYP4F2, '
            'elevando los niveles de vitamina K y requiriendo dosis más altas '
            'de warfarina (anticoagulante) para el mismo efecto. '
            'Información relevante para quienes toman anticoagulantes.'
        ),
        'interpretations': {
            'CC': {'result': 'CYP4F2 normal', 'emoji': '💊', 'detail': 'Metabolismo de vitamina K estándar. Dosis normales de warfarina.'},
            'CT': {'result': 'CYP4F2 moderadamente reducido', 'emoji': '⚗️', 'detail': 'Ligero aumento en niveles de vitamina K. Puede necesitar ajuste leve de anticoagulante.'},
            'TT': {'result': 'CYP4F2 reducido', 'emoji': '⚠️', 'detail': 'Niveles elevados de vitamina K. Puede requerir dosis más altas de warfarina. Importante informar al médico.'},
        },
        'fun_fact': 'La warfarina fue originalmente desarrollada como veneno para ratas. Luego se descubrió que en dosis bajas previene coágulos en humanos. ¡Los mejores medicamentos a veces tienen orígenes sorprendentes! 🐀'
    },

    'rs1800864': {
        'rsid': 'rs1800864',
        'gene': 'NAT2',
        'category': 'Metabolismo',
        'subcategory': 'Medicamentos',
        'title': 'Acetilación de fármacos (NAT2)',
        'description': (
            'El gen NAT2 codifica la N-acetiltransferasa 2, '
            'que metaboliza medicamentos como isoniazida (tuberculosis), '
            'procainamida (arritmias) e hidralazina (presión arterial). '
            'Este SNP determina si eres un acetilador rápido o lento.'
        ),
        'interpretations': {
            'GG': {'result': 'Acetilador rápido NAT2', 'emoji': '⚡', 'detail': 'Metabolismo rápido de isoniazida y otros sustratos NAT2. Dosis estándar puede ser insuficiente.'},
            'AG': {'result': 'Acetilador intermedio', 'emoji': '⚖️', 'detail': 'Velocidad de acetilación intermedia. Respuesta estándar a la mayoría de medicamentos.'},
            'AA': {'result': 'Acetilador lento NAT2', 'emoji': '🐌', 'detail': 'Metabolismo lento. Los fármacos NAT2-dependientes se acumulan. Mayor riesgo de efectos secundarios con isoniazida.'},
        },
        'fun_fact': 'Los acetiladores lentos de NAT2 tienen mayor riesgo de lupus inducido por medicamentos. Esto se descubrió en soldados americanos que tomaban hidralazina durante la Guerra de Corea. 💊'
    },

    'rs2395029': {
        'rsid': 'rs2395029',
        'gene': 'HCP5',
        'category': 'Salud',
        'subcategory': 'Sistema inmune',
        'title': 'Hipersensibilidad al abacavir (HCP5)',
        'description': (
            'El gen HCP5 es un marcador proxy del alelo HLA-B*57:01. '
            'La presencia del alelo G es un predictor de hipersensibilidad grave '
            'al abacavir, un antirretroviral usado en el tratamiento del VIH. '
            'El test genético de este SNP es estándar antes de prescribir abacavir.'
        ),
        'interpretations': {
            'TT': {'result': 'Sin riesgo de hipersensibilidad al abacavir', 'emoji': '✅', 'detail': 'Sin el alelo de riesgo HLA-B*57:01. El abacavir puede usarse con precauciones estándar.'},
            'GT': {'result': 'Portador de riesgo', 'emoji': '⚠️', 'detail': 'Portador de un alelo G. Alto riesgo de reacción de hipersensibilidad al abacavir. Debe evitarse.'},
            'GG': {'result': 'Alto riesgo de hipersensibilidad', 'emoji': '🚫', 'detail': 'Marcador de HLA-B*57:01. El abacavir está contraindicado. Informar siempre al médico.'},
        },
        'fun_fact': 'El cribado genético de este SNP antes de prescribir abacavir ha salvado miles de vidas al evitar reacciones alérgicas graves. Es uno de los mejores ejemplos de medicina personalizada en acción. 💊'
    },

    'rs10811661': {
        'rsid': 'rs10811661',
        'gene': 'CDKN2A/CDKN2B',
        'category': 'Salud',
        'subcategory': 'Diabetes tipo 2',
        'title': 'Riesgo de diabetes tipo 2 (CDKN2A/B)',
        'description': (
            'Este SNP en la región de los genes CDKN2A/CDKN2B está asociado '
            'con el riesgo de diabetes tipo 2 a través de la regulación '
            'de la masa y función de las células beta pancreáticas. '
            'El alelo T de riesgo está asociado a mayor riesgo de DM2.'
        ),
        'interpretations': {
            'CC': {'result': 'Sin riesgo adicional', 'emoji': '✅', 'detail': 'Sin el alelo de riesgo en esta región. Riesgo basal de DM2.'},
            'CT': {'result': 'Riesgo levemente aumentado', 'emoji': '🍎', 'detail': 'Un alelo T. Riesgo moderado. La dieta y el ejercicio son los factores más modificables.'},
            'TT': {'result': 'Riesgo aumentado de DM2', 'emoji': '🩺', 'detail': 'Dos alelos T. Mayor riesgo genético de DM2. El estilo de vida saludable puede reducirlo significativamente.'},
        },
        'fun_fact': 'El páncreas tiene una reserva de células beta que puede reponerse con el ejercicio. ¡Cada sesión de ejercicio es una inversión en tu páncreas! 🏋️'
    },

    'rs2260000': {
        'rsid': 'rs2260000',
        'gene': 'CYP1B1',
        'category': 'Metabolismo',
        'subcategory': 'Metabolismo hormonal',
        'title': 'Metabolismo de estrógenos (CYP1B1)',
        'description': (
            'El gen CYP1B1 metaboliza los estrógenos y otros compuestos. '
            'Las variantes de CYP1B1 afectan la producción de catecolestrógenos '
            'y pueden influir en el riesgo hormono-dependiente. '
            'También regula el metabolismo de compuestos ambientales (xenobióticos).'
        ),
        'interpretations': {
            'CC': {'result': 'CYP1B1 forma estándar', 'emoji': '⚖️', 'detail': 'Función enzimática estándar. Metabolismo hormonal normal.'},
            'CT': {'result': 'CYP1B1 variante heterocigota', 'emoji': '🔬', 'detail': 'Actividad enzimática intermedia.'},
            'TT': {'result': 'CYP1B1 variante homocigota', 'emoji': '🧪', 'detail': 'Actividad enzimática modificada. Puede influir en el metabolismo de estrógenos y xenobióticos.'},
        },
        'fun_fact': 'CYP1B1 fue el primer gen asociado al glaucoma congénito. ¡Una enzima de metabolismo hormonal también protege los ojos! 👁️'
    },

    'rs2228479': {
        'rsid': 'rs2228479',
        'gene': 'MC1R',
        'category': 'Rasgo',
        'subcategory': 'Color de cabello',
        'title': 'Variante MC1R adicional (V92M)',
        'description': (
            'Segunda variante funcional del receptor de melanocortina 1 (MC1R). '
            'La variante V92M (rs2228479, alelo G) tiene efecto más leve que R151C (rs1805007), '
            'pero puede combinarse con otras variantes para aumentar el riesgo de fenotipo de piel clara o cabello rubio.'
        ),
        'interpretations': {
            'AA': {'result': 'MC1R V92M normal', 'emoji': '🖤', 'detail': 'Sin variante V92M. Receptor MC1R normal en este locus.'},
            'AG': {'result': 'Portador V92M', 'emoji': '🟡', 'detail': 'Un alelo G. Ligera modificación en la función MC1R. Posibles reflejos dorados o piel algo más clara.'},
            'GG': {'result': 'Homocigoto V92M', 'emoji': '👱', 'detail': 'Dos alelos G. Mayor impacto en la pigmentación. Posible asociación a cabello rubio o castaño claro.'},
        },
        'fun_fact': 'El gen MC1R tiene más de 200 variantes conocidas. ¡Es el gen más variable de la pigmentación humana y explica por qué hay tantos matices de color de cabello! 💇'
    },

    'rs17822931': {
        'rsid': 'rs17822931',
        'gene': 'ABCC11',
        'category': 'Rasgo',
        'subcategory': 'Rasgos físicos',
        'title': 'Tipo de cerumen y olor corporal (ABCC11)',
        'description': (
            'El gen ABCC11 codifica un transportador de membrana que determina '
            'si el cerumen (cera del oído) es húmedo o seco, '
            'y también el olor corporal axilar. '
            'El alelo T produce cerumen seco y menor olor axilar. '
            'El alelo C produce cerumen húmedo y mayor olor corporal. '
            'El alelo T es casi universal en asiáticos del este, '
            'mientras que el C predomina en europeos y africanos.'
        ),
        'interpretations': {
            'TT': {'result': 'Cerumen seco / bajo olor axilar', 'emoji': '🧊', 'detail': 'Cerumen seco y escamoso. Menor olor corporal axilar. Marcador de ancestría del este asiático. Los desodorantes son menos necesarios.'},
            'CT': {'result': 'Portador mixto', 'emoji': '💧', 'detail': 'Un alelo C. Cerumen intermedio. Olor axilar moderado.'},
            'CC': {'result': 'Cerumen húmedo / olor axilar normal', 'emoji': '🌊', 'detail': 'Cerumen húmedo. Olor axilar normal. Frecuente en europeos y africanos. Los desodorantes son útiles.'},
        },
        'fun_fact': 'En Japón, el alelo T (cerumen seco) es tan universal que los otorrinolaringólogos japoneses desconocían la existencia del cerumen húmedo hasta que empezaron a tratar pacientes extranjeros. 😂'
    },

    'rs4149056': {
        'rsid': 'rs4149056',
        'gene': 'SLCO1B1',
        'category': 'Metabolismo',
        'subcategory': 'Medicamentos',
        'title': 'Intolerancia a las estatinas (SLCO1B1)',
        'description': (
            'El gen SLCO1B1 codifica un transportador hepático que importa estatinas '
            'a las células del hígado. '
            'La variante C (rs4149056) reduce la función del transportador, '
            'aumentando la concentración de estatinas en sangre '
            'y el riesgo de miopatía (daño muscular) como efecto secundario.'
        ),
        'interpretations': {
            'TT': {'result': 'Metabolismo normal de estatinas', 'emoji': '✅', 'detail': 'Transportador SLCO1B1 funcional. Las estatinas se procesan normalmente. Bajo riesgo de miopatía.'},
            'CT': {'result': 'Riesgo moderado de miopatía', 'emoji': '⚠️', 'detail': 'Un alelo C. Riesgo moderadamente aumentado de efectos secundarios musculares con estatinas.'},
            'CC': {'result': 'Alto riesgo de miopatía por estatinas', 'emoji': '🚨', 'detail': 'Dos alelos C. Riesgo muy aumentado de miopatía con estatinas (especialmente simvastatina alta dosis). Informar al médico.'},
        },
        'fun_fact': 'El 10-25% de los pacientes que dejan de tomar estatinas lo hacen por dolor muscular. El test de SLCO1B1 puede identificar quiénes tienen mayor riesgo antes de empezar el tratamiento. 💊'
    },

    'rs9282564': {
        'rsid': 'rs9282564',
        'gene': 'ABCB1',
        'category': 'Metabolismo',
        'subcategory': 'Medicamentos',
        'title': 'Absorción de medicamentos (ABCB1/MDR1)',
        'description': (
            'El gen ABCB1 (Multidrug Resistance 1, MDR1) codifica la glicoproteína-P, '
            'una bomba de expulsión que reduce la absorción intestinal de muchos medicamentos '
            'y protege el cerebro (barrera hematoencefálica). '
            'Las variantes de ABCB1 afectan la eficacia y toxicidad de numerosos fármacos.'
        ),
        'interpretations': {
            'AA': {'result': 'ABCB1 funcional normal', 'emoji': '💊', 'detail': 'Glicoproteína-P normal. Absorción y distribución de medicamentos estándar.'},
            'AG': {'result': 'ABCB1 moderadamente alterado', 'emoji': '⚗️', 'detail': 'Variación en la función de la glicoproteína-P. Puede haber diferencias en la absorción de algunos fármacos.'},
            'GG': {'result': 'ABCB1 variante', 'emoji': '🔬', 'detail': 'Función alterada de glicoproteína-P. Posible mayor biodisponibilidad oral de sustratos (digoxina, antidepresivos, antiepilépticos).'},
        },
        'fun_fact': 'La glicoproteína-P es una de las razones por las que algunos medicamentos no funcionan igual en todos. ¡Es literalmente una bomba molecular en tus células intestinales! 🔬'
    },

    'rs1801282': {
        'rsid': 'rs1801282',
        'gene': 'PPARG',
        'category': 'Metabolismo',
        'subcategory': 'Sensibilidad a la insulina',
        'title': 'Sensibilidad a la insulina (PPARG Pro12Ala)',
        'description': (
            'PPARG (receptor gamma activado por proliferadores de peroxisomas) '
            'regula la diferenciación de adipocitos y la sensibilidad a la insulina. '
            'La variante Ala (G en rs1801282) está asociada paradójicamente '
            'a MAYOR sensibilidad a la insulina y MENOR riesgo de diabetes tipo 2, '
            'a pesar de ser la variante "alternativa".'
        ),
        'interpretations': {
            'CC': {'result': 'Pro12/Pro12 - mayor riesgo DM2', 'emoji': '⚖️', 'detail': 'La forma más común. Sensibilidad a la insulina estándar. Mayor riesgo de DM2 que los portadores de G.'},
            'CG': {'result': 'Pro12/Ala12 - protector moderado', 'emoji': '🌱', 'detail': 'Un alelo Ala. Mayor sensibilidad a la insulina. Riesgo de DM2 reducido.'},
            'GG': {'result': 'Ala12/Ala12 - máxima protección', 'emoji': '✅', 'detail': 'Dos alelos Ala. Mayor sensibilidad a la insulina. Menor riesgo de DM2 y síndrome metabólico.'},
        },
        'fun_fact': 'El gen PPARG es la diana de las tiazolidinedionas (medicamentos para la diabetes). ¡Tu variante de PPARG puede determinar cuánto se beneficia tu cuerpo de ciertos antidiabéticos! 💊'
    },

    'rs5174': {
        'rsid': 'rs5174',
        'gene': 'LDLR',
        'category': 'Salud',
        'subcategory': 'Colesterol LDL',
        'title': 'Receptor LDL y colesterol (LDLR)',
        'description': (
            'El gen LDLR codifica el receptor de LDL, que captura el "colesterol malo" '
            'de la sangre y lo introduce en las células. '
            'Variantes en LDLR pueden afectar la eficiencia de este proceso, '
            'influyendo en los niveles de LDL circulante.'
        ),
        'interpretations': {
            'CC': {'result': 'LDLR estándar', 'emoji': '💙', 'detail': 'Receptor LDL de función normal. Niveles de LDL en rango esperado según dieta.'},
            'CT': {'result': 'LDLR variante moderada', 'emoji': '⚖️', 'detail': 'Ligera variación en eficiencia del receptor LDL.'},
            'TT': {'result': 'LDLR variante', 'emoji': '🔬', 'detail': 'Variante del receptor LDL. Posible diferencia en aclaramiento de LDL. Monitorear colesterol periódicamente.'},
        },
        'fun_fact': 'Joseph Goldstein y Michael Brown ganaron el Nobel 1985 por descubrir el receptor LDL. Sus investigaciones revolucionaron el tratamiento de las enfermedades cardiovasculares. 🏆'
    },

    'rs2294008': {
        'rsid': 'rs2294008',
        'gene': 'PSCA',
        'category': 'Salud',
        'subcategory': 'Sistema digestivo',
        'title': 'Antígeno de células madre prostáticas (PSCA)',
        'description': (
            'El gen PSCA regula la proliferación de células epiteliales del estómago. '
            'La variante T en rs2294008 está asociada a mayor riesgo de cáncer gástrico, '
            'especialmente en combinación con infección por H. pylori. '
            'También afecta la susceptibilidad a úlceras gástricas.'
        ),
        'interpretations': {
            'CC': {'result': 'Sin alelo de riesgo gástrico', 'emoji': '✅', 'detail': 'Sin el marcador de riesgo PSCA. Susceptibilidad estándar a enfermedades gástricas.'},
            'CT': {'result': 'Riesgo moderado gástrico', 'emoji': '🌶️', 'detail': 'Un alelo T. Riesgo moderadamente aumentado. Monitorear si hay infección por H. pylori.'},
            'TT': {'result': 'Riesgo aumentado gástrico', 'emoji': '⚠️', 'detail': 'Dos alelos T. Mayor susceptibilidad a problemas gástricos. Erradicación de H. pylori si está presente es importante.'},
        },
        'fun_fact': '¡H. pylori fue considerada durante décadas un mito! Hasta que Barry Marshall se la bebió para demostrar que causaba úlceras, ganando el Nobel de Medicina 2005. 🦠'
    },

    'rs10993994': {
        'rsid': 'rs10993994',
        'gene': 'MSMB',
        'category': 'Salud',
        'subcategory': 'Próstata',
        'title': 'Marcador de salud prostática (MSMB)',
        'description': (
            'El gen MSMB (Microseminoprotein-beta) está involucrado en la regulación del crecimiento prostático. '
            'El alelo T en rs10993994 está asociado con niveles más bajos de PSP94 '
            'y un riesgo modestamente aumentado de cáncer de próstata. '
            'Información educativa solamente. Solo para hombres biológicos.'
        ),
        'interpretations': {
            'CC': {'result': 'Sin alelo de riesgo MSMB', 'emoji': '✅', 'detail': 'Alelo protector. Niveles normales de PSP94.'},
            'CT': {'result': 'Riesgo moderado MSMB', 'emoji': '🔬', 'detail': 'Un alelo T. Ligero aumento en susceptibilidad. Screenings regulares recomendados.'},
            'TT': {'result': 'Mayor susceptibilidad MSMB', 'emoji': '⚠️', 'detail': 'Dos alelos T. Mayor susceptibilidad. Seguimiento médico y estilo de vida saludable importantes.'},
        },
        'fun_fact': 'El PSA (marcador de próstata) fue descubierto en 1979 y ha salvado millones de vidas al permitir diagnóstico precoz. La genética está mejorando aún más su precisión. 🔬'
    },

    'rs4939827': {
        'rsid': 'rs4939827',
        'gene': 'SMAD7',
        'category': 'Salud',
        'subcategory': 'Sistema digestivo',
        'title': 'Riesgo de cáncer colorrectal (SMAD7)',
        'description': (
            'El gen SMAD7 es un regulador negativo de la señalización de TGF-β. '
            'El alelo T en rs4939827 está asociado a mayor riesgo de cáncer colorrectal. '
            'SMAD7 también juega un papel en la enfermedad inflamatoria intestinal. '
            'Información educativa. La colonoscopia preventiva es la mejor herramienta de screening.'
        ),
        'interpretations': {
            'CC': {'result': 'Sin alelo de riesgo SMAD7', 'emoji': '✅', 'detail': 'Sin el marcador de riesgo de cáncer colorrectal en SMAD7.'},
            'CT': {'result': 'Riesgo moderadamente aumentado', 'emoji': '🌿', 'detail': 'Un alelo T. Riesgo ligeramente aumentado. Dieta rica en fibra y colonoscopia preventiva recomendadas.'},
            'TT': {'result': 'Riesgo aumentado de CCR', 'emoji': '⚠️', 'detail': 'Dos alelos T. Mayor susceptibilidad. Colonoscopia preventiva y dieta con alta fibra son especialmente importantes.'},
        },
        'fun_fact': 'Una dieta rica en fibra reduce el riesgo de cáncer colorrectal hasta un 40%. Las bacterias intestinales que fermentan la fibra producen butirato, que protege las células del colon. 🥦'
    },

    'rs1800896': {
        'rsid': 'rs1800896',
        'gene': 'IL10',
        'category': 'Salud',
        'subcategory': 'Sistema inmune',
        'title': 'Interleucina 10 anti-inflamatoria (IL-10)',
        'description': (
            'La IL-10 es una potente citoquina anti-inflamatoria. '
            'La variante A en rs1800896 está asociada a mayor producción de IL-10, '
            'lo que puede ser protector en enfermedades inflamatorias crónicas '
            'pero podría reducir la eficacia de la respuesta inmune contra ciertas infecciones.'
        ),
        'interpretations': {
            'GG': {'result': 'Menor producción de IL-10', 'emoji': '🔥', 'detail': 'Producción reducida de IL-10. Respuesta inflamatoria más activa. Mayor eficacia anti-infecciosa, mayor riesgo de inflamación crónica.'},
            'AG': {'result': 'Producción intermedia de IL-10', 'emoji': '⚖️', 'detail': 'Equilibrio entre respuesta inflamatoria y anti-inflamatoria.'},
            'AA': {'result': 'Alta producción de IL-10', 'emoji': '🌿', 'detail': 'Mayor producción de IL-10. Mejor regulación inmune. Protección frente a enfermedades autoinmunes e inflamatorias crónicas.'},
        },
        'fun_fact': 'La IL-10 fue bautizada como "el factor supresor de la síntesis de citoquinas" antes de conocerse su estructura. ¡Es el sistema de frenado del sistema inmune! 🚦'
    },

    'rs7756992': {
        'rsid': 'rs7756992',
        'gene': 'CDKAL1',
        'category': 'Salud',
        'subcategory': 'Diabetes tipo 2',
        'title': 'Función de células beta (CDKAL1)',
        'description': (
            'CDKAL1 (CDK5 Regulatory Subunit Associated Protein 1-like 1) '
            'regula la función de las células beta del páncreas. '
            'El alelo G de riesgo en rs7756992 reduce la función de las células beta, '
            'disminuyendo la secreción de insulina en respuesta a la glucosa.'
        ),
        'interpretations': {
            'AA': {'result': 'Sin riesgo adicional CDKAL1', 'emoji': '✅', 'detail': 'Función normal de células beta en este locus.'},
            'AG': {'result': 'Riesgo moderado DM2 (CDKAL1)', 'emoji': '🍎', 'detail': 'Un alelo G. Ligera reducción en función de células beta.'},
            'GG': {'result': 'Riesgo aumentado DM2 (CDKAL1)', 'emoji': '🩺', 'detail': 'Dos alelos G. Función de células beta reducida. Mayor susceptibilidad a DM2. El ejercicio mejora la sensibilidad a la insulina.'},
        },
        'fun_fact': 'Las células beta del páncreas son tan delicadas que no pueden regenerarse fácilmente. ¡Protegerlas con ejercicio y dieta desde joven es la mejor medicina preventiva! 🥗'
    },

    'rs2237892': {
        'rsid': 'rs2237892',
        'gene': 'KCNQ1',
        'category': 'Salud',
        'subcategory': 'Diabetes tipo 2',
        'title': 'Canal de potasio y diabetes (KCNQ1)',
        'description': (
            'KCNQ1 codifica un canal de potasio expresado en células beta pancreáticas '
            'que regula la secreción de insulina. '
            'La variante C en rs2237892 está fuertemente asociada a mayor riesgo de DM2, '
            'especialmente en poblaciones asiáticas.'
        ),
        'interpretations': {
            'TT': {'result': 'Sin riesgo adicional KCNQ1', 'emoji': '✅', 'detail': 'Canal de potasio normal. Secreción de insulina estándar.'},
            'CT': {'result': 'Riesgo moderado DM2 (KCNQ1)', 'emoji': '🍎', 'detail': 'Un alelo C. Ligera reducción en la secreción de insulina.'},
            'CC': {'result': 'Riesgo aumentado DM2 (KCNQ1)', 'emoji': '🩺', 'detail': 'Canal de potasio alterado. Mayor susceptibilidad a DM2. Control glucémico preventivo recomendado.'},
        },
        'fun_fact': 'Los canales de potasio KCNQ1 también regulan el ritmo cardíaco. ¡Un mismo canal iónico une el corazón y el páncreas en el riesgo de enfermedades metabólicas! ❤️'
    },

    'rs1801394': {
        'rsid': 'rs1801394',
        'gene': 'MTRR',
        'category': 'Metabolismo',
        'subcategory': 'Vitamina B12 y folato',
        'title': 'Regeneración de metionina (MTRR A66G)',
        'description': (
            'El gen MTRR codifica la metionina sintasa reductasa, '
            'que regenera la forma activa de la vitamina B12 necesaria para el ciclo de la metionina. '
            'La variante G (rs1801394) puede reducir la eficiencia de este proceso, '
            'aumentando el riesgo de niveles elevados de homocisteína, '
            'especialmente con niveles bajos de B12.'
        ),
        'interpretations': {
            'AA': {'result': 'MTRR funcional normal', 'emoji': '✅', 'detail': 'Regeneración eficiente de B12 activa. Metabolismo de la metionina normal.'},
            'AG': {'result': 'MTRR moderadamente reducida', 'emoji': '🔶', 'detail': 'Un alelo G. Ligera reducción en la regeneración de B12. Asegurar niveles adecuados de B12 en dieta.'},
            'GG': {'result': 'MTRR reducida', 'emoji': '💊', 'detail': 'Reducción en la regeneración de B12 activa. Mayor riesgo de hiperhomocisteinemia con dieta baja en B12. Suplementar si es vegetariano/vegano.'},
        },
        'fun_fact': 'La vitamina B12 solo se encuentra naturalmente en alimentos de origen animal. ¡Los veganos con variantes MTRR reducida tienen doble necesidad de suplementar esta vitamina! 🌿'
    },

    'rs1800971': {
        'rsid': 'rs1800971',
        'gene': 'CYP3A4',
        'category': 'Metabolismo',
        'subcategory': 'Medicamentos',
        'title': 'Metabolismo de medicamentos (CYP3A4)',
        'description': (
            'CYP3A4 es la enzima de metabolismo hepático más importante, '
            'procesando el 50% de todos los medicamentos. '
            'Incluye estatinas, antidepresivos, antihistamínicos, antibióticos y muchos más. '
            'Las variantes de CYP3A4 pueden afectar la eficacia y seguridad de la mayoría de tratamientos farmacológicos.'
        ),
        'interpretations': {
            'TT': {'result': 'CYP3A4 normal', 'emoji': '💊', 'detail': 'Actividad enzimática estándar. Dosis normales de medicamentos CYP3A4-dependientes.'},
            'CT': {'result': 'CYP3A4 variante moderada', 'emoji': '⚗️', 'detail': 'Actividad enzimática ligeramente modificada. Posibles diferencias en efectos de algunos fármacos.'},
            'CC': {'result': 'CYP3A4 variante', 'emoji': '🔬', 'detail': 'Variante en CYP3A4. Importante informar al médico y farmacéutico para optimizar dosis de medicamentos.'},
        },
        'fun_fact': 'El zumo de pomelo inhibe CYP3A4 y puede multiplicar por 10 la concentración de algunos medicamentos en sangre. ¡Por eso algunos medicamentos dicen "no tomar con pomelo"! 🍊'
    },

    'rs8050136': {
        'rsid': 'rs8050136',
        'gene': 'FTO',
        'category': 'Salud',
        'subcategory': 'Peso corporal',
        'title': 'Tercera variante FTO (rs8050136)',
        'description': (
            'Tercera variante del gen FTO en alta vinculación desequilibrada con rs9939609. '
            'También está asociada a IMC, apetito y riesgo de obesidad. '
            'El alelo A está asociado a mayor riesgo.'
        ),
        'interpretations': {
            'CC': {'result': 'Sin riesgo FTO adicional', 'emoji': '✅', 'detail': 'Sin el tercer marcador de riesgo FTO. Alelo protector.'},
            'AC': {'result': 'Riesgo moderado FTO (rs8050136)', 'emoji': '⚖️', 'detail': 'Un alelo A. Ligero aumento en tendencia al sobrepeso.'},
            'AA': {'result': 'Riesgo aumentado FTO (rs8050136)', 'emoji': '⚠️', 'detail': 'Dos alelos A. El ejercicio aeróbico regular compensa este riesgo genético.'},
        },
        'fun_fact': 'El gen FTO fue descubierto en 2007 y rápidamente se convirtió en el gen de obesidad más estudiado del mundo. ¡En 15 años acumuló más de 5.000 publicaciones científicas! 📚'
    },

    'rs10757278': {
        'rsid': 'rs10757278',
        'gene': 'CDKN2B-AS1 (9p21.3)',
        'category': 'Salud',
        'subcategory': 'Cardiovascular',
        'title': 'Riesgo de enfermedad coronaria e infarto (Locus 9p21)',
        'description': (
            'El locus 9p21.3 es el factor genético más replicado para enfermedad coronaria e infarto de miocardio. '
            'No codifica una proteína sino un ARN largo no codificante (ANRIL) que modula la proliferación celular '
            'y la inflamación en la pared arterial. El alelo G aumenta el riesgo coronario en ~30-40% por alelo.'
        ),
        'interpretations': {
            'AA': {'result': 'Riesgo coronario basal / estándar', 'emoji': '🫀', 'detail': 'Sin el alelo de riesgo 9p21. Riesgo genético coronario basal poblacional.'},
            'AG': {'result': 'Riesgo coronario moderadamente aumentado', 'emoji': '⚠️', 'detail': 'Un alelo G (+30% riesgo relativo). El ejercicio aeróbico regular, dieta mediterránea y control de tensión arterial compensan fuertemente este riesgo.'},
            'GG': {'result': 'Mayor susceptibilidad a cardiopatía isquémica', 'emoji': '🚨', 'detail': 'Dos alelos G (+60% riesgo relativo). Especial importancia al control de colesterol LDL, presión arterial y evitar el tabaquismo.'},
        },
        'fun_fact': 'Estudios de intervención demostraron que llevar una dieta alta en frutas y verduras crudas anula casi por completo el riesgo añadido por este locus genético. ¡La nutrición apaga el riesgo! 🥗'
    },

    'rs699': {
        'rsid': 'rs699',
        'gene': 'AGT',
        'category': 'Salud',
        'subcategory': 'Presión arterial',
        'title': 'Predisposición a hipertensión sensible a la sal (AGT M235T)',
        'description': (
            'El gen AGT codifica el angiotensinógeno, el primer eslabón del sistema renina-angiotensina. '
            'La variante C (Treonina en posición 235) se asocia a concentraciones plasmáticas más elevadas de angiotensinógeno '
            'y una mayor sensibilidad de la presión arterial al consumo de sodio dietético.'
        ),
        'interpretations': {
            'TT': {'result': 'Baja sensibilidad de tensión arterial al sodio', 'emoji': '✅', 'detail': 'Niveles estándar de angiotensinógeno. Presión arterial menos susceptible a variaciones en la ingesta de sal.'},
            'CT': {'result': 'Sensibilidad moderada a la sal', 'emoji': '🧂', 'detail': 'Un alelo C. Moderar el consumo de sal procesada (<5 g/día) ayuda a mantener cifras tensionales óptimas.'},
            'CC': {'result': 'Hipertensión sensible a la sal', 'emoji': '⚠️', 'detail': 'Dos alelos C. Mayor predisposición a hipertensión arterial. Muy alta respuesta positiva a dietas tipo DASH (bajas en sodio y ricas en potasio).'},
        },
        'fun_fact': 'Esta variante era ventajosa en el Paleolítico para evitar la deshidratación y retener sales escasas. Hoy, con la abundancia de alimentos ultraprocesados, se traduce en hipertensión. 🌊'
    },

    'rs6025': {
        'rsid': 'rs6025',
        'gene': 'F5',
        'category': 'Salud',
        'subcategory': 'Trombosis y coagulación',
        'title': 'Trombofilia por Factor V Leiden (F5 R506Q)',
        'description': (
            'El Factor V Leiden es la causa genética más frecuente de trombofilia hereditaria. '
            'La mutación (alelo A) hace que el factor V de la coagulación sea resistente a la inactivación por la proteína C, '
            'aumentando el riesgo de trombosis venosa profunda (TVP) y tromboembolismo pulmonar.'
        ),
        'interpretations': {
            'GG': {'result': 'Sin variante Factor V Leiden', 'emoji': '✅', 'detail': 'Coagulación normal. Sin riesgo aumentado de trombosis venosa por este marcador principal.'},
            'AG': {'result': 'Portador heterocigoto Factor V Leiden', 'emoji': '⚠️', 'detail': 'Riesgo 3 a 7 veces mayor de trombosis venosa. Muy importante notificar a médicos antes de cirugías mayores, inmovilizaciones o uso de estrógenos orales.'},
            'AA': {'result': 'Homocigoto Factor V Leiden', 'emoji': '🚨', 'detail': 'Riesgo marcadamente elevado de eventos trombóticos venosos. Requiere asesoramiento y seguimiento hematológico.'},
        },
        'fun_fact': 'Aproximadamente el 5% de las personas de ascendencia europea portan esta variante. Históricamente protegía contra hemorragias mortales en partos y heridas de combate. 🩸'
    },

    'rs1799963': {
        'rsid': 'rs1799963',
        'gene': 'F2',
        'category': 'Salud',
        'subcategory': 'Trombosis y coagulación',
        'title': 'Mutación de Protrombina G20210A (Factor II)',
        'description': (
            'La variante G20210A en la región 3\' UTR del gen de la protrombina aumenta la síntesis de factor II en ~30%, '
            'constituyendo la segunda causa más frecuente de trombofilia hereditaria en poblaciones de origen europeo.'
        ),
        'interpretations': {
            'GG': {'result': 'Sin mutación de protrombina G20210A', 'emoji': '✅', 'detail': 'Niveles normales de protrombina. Sin riesgo trombótico añadido por este gen.'},
            'AG': {'result': 'Portador de mutación protrombina G20210A', 'emoji': '⚠️', 'detail': 'Riesgo 2 a 3 veces mayor de trombosis venosa profunda. Se recomiendan medidas preventivas en viajes de larga duración o reposo prolongado.'},
            'AA': {'result': 'Homocigoto protrombina G20210A', 'emoji': '🚨', 'detail': 'Riesgo significativamente aumentado de trombosis. Evaluación hematológica preventiva recomendada.'},
        },
        'fun_fact': 'Surgió en un único individuo hace unos 24.000 años y se expandió por toda Europa. ¡Una pequeña mutación que cambió la coagulación de millones de personas! 🧬'
    },

    'rs1061170': {
        'rsid': 'rs1061170',
        'gene': 'CFH',
        'category': 'Salud',
        'subcategory': 'Visión y retina',
        'title': 'Degeneración macular asociada a la edad (CFH Y402H)',
        'description': (
            'El gen CFH (Factor H del Complemento) previene el ataque autoinmune contra la retina. '
            'La variante C (Tirosina→Histidina en codón 402) disminuye la regulación antiinflamatoria en la mácula, '
            'siendo el principal factor de riesgo genético para degeneración macular asociada a la edad (DMAE).'
        ),
        'interpretations': {
            'TT': {'result': 'Bajo riesgo genético de DMAE', 'emoji': '👁️', 'detail': 'Factor H plenamente funcional en la retina. Riesgo basal estándar de degeneración macular.'},
            'CT': {'result': 'Riesgo moderadamente aumentado de DMAE', 'emoji': '👓', 'detail': 'Riesgo ~2.5 veces mayor. Estrategias de protección demostradas: gafas de sol con filtro UV, dieta rica en luteína/zeaxantina y evitar estrictamente fumar.'},
            'CC': {'result': 'Mayor susceptibilidad a DMAE', 'emoji': '⚠️', 'detail': 'Riesgo ~5-6 veces mayor. Es aconsejable realizar revisiones de fondo de ojo a partir de los 50 años y asegurar antioxidantes carotenoides en la dieta.'},
        },
        'fun_fact': 'El tabaquismo y este gen interactúan de forma multiplicativa: fumar multiplica por 5 el riesgo de pérdida visual en portadores de la variante CC. ¡No fumar protege la visión! 🥦'
    },

    'rs1544410': {
        'rsid': 'rs1544410',
        'gene': 'VDR',
        'category': 'Salud',
        'subcategory': 'Hueso y articulaciones',
        'title': 'Receptor de Vitamina D y densidad ósea (VDR BsmI)',
        'description': (
            'El receptor de vitamina D (VDR) regula la absorción intestinal de calcio y la remodelación del tejido óseo. '
            'El polimorfismo BsmI (alelo A) se asocia a menor densidad mineral ósea y mayor susceptibilidad a osteopenia en la madurez.'
        ),
        'interpretations': {
            'GG': {'result': 'Densidad mineral ósea favorable', 'emoji': '🦴', 'detail': 'Excelente respuesta a la vitamina D para la absorción de calcio. Menor riesgo de osteopenia.'},
            'AG': {'result': 'Densidad ósea intermedia', 'emoji': '⚖️', 'detail': 'Respuesta intermedia. Mantener niveles suficientes de vitamina D3 y realizar ejercicio de fuerza es protector.'},
            'AA': {'result': 'Mayor susceptibilidad a osteopenia / osteoporosis', 'emoji': '⚠️', 'detail': 'Menor densidad ósea media. Recomendable controlar niveles séricos de 25-OH vitamina D y priorizar entrenamiento de fuerza con sobrecarga.'},
        },
        'fun_fact': 'El ejercicio de fuerza (levantar peso) genera fuerzas piezoeléctricas en el hueso que activan a los osteoblastos, compensando con creces la predisposición genética. 🏋️'
    },

    'rs34637584': {
        'rsid': 'rs34637584',
        'gene': 'LRRK2',
        'category': 'Salud',
        'subcategory': 'Neurología',
        'title': 'Variante LRRK2 G2019S (Parkinson hereditario)',
        'description': (
            'La mutación G2019S en el gen LRRK2 es la causa genética monogénica más frecuente de enfermedad de Parkinson. '
            'Es una mutación con penetrancia incompleta (~25-30% de los portadores la desarrollan a lo largo de su vida).'
        ),
        'interpretations': {
            'GG': {'result': 'Negativo para LRRK2 G2019S', 'emoji': '✅', 'detail': 'Sin la variante de riesgo LRRK2 G2019S. Riesgo genético estándar.'},
            'AG': {'result': 'Portador de variante LRRK2 G2019S', 'emoji': '🩺', 'detail': 'Portador de un alelo de riesgo. La penetrancia es incompleta (muchos portadores nunca desarrollan la enfermedad). Recomendable asesoramiento genético especializado.'},
            'AA': {'result': 'Homocigoto LRRK2 G2019S', 'emoji': '🚨', 'detail': 'Dos alelos de la variante LRRK2 G2019S. Muy poco frecuente. Asesoramiento genético médico recomendado.'},
        },
        'fun_fact': 'Esta variante es especialmente frecuente en personas de origen bereber/norteafricano (hasta un 30-40% de casos de Parkinson) y en judíos asquenazíes (15-20%). 🌍'
    },

    'rs2476601': {
        'rsid': 'rs2476601',
        'gene': 'PTPN22',
        'category': 'Salud',
        'subcategory': 'Autoinmunidad',
        'title': 'Predisposición autoinmune general (PTPN22 R620W)',
        'description': (
            'El gen PTPN22 codifica la proteína tirosina fosfatasa no receptora 22 (Lyp), que actúa como "freno" de los linfocitos T. '
            'La variante T (Trp620) debilita este freno, facilitando que el sistema inmune ataque tejidos propios '
            '(artritis reumatoide, tiroiditis autoinmune de Hashimoto, vitíligo, diabetes tipo 1).'
        ),
        'interpretations': {
            'CC': {'result': 'Regulación inmunitaria normal', 'emoji': '🛡️', 'detail': 'Sin el alelo de riesgo autoinmune PTPN22. Umbral de tolerancia de linfocitos T adecuado.'},
            'CT': {'result': 'Portador de alelo autoinmune PTPN22', 'emoji': '⚠️', 'detail': 'Un alelo T. Mayor propensión a trastornos autoinmunes (tiroides, articulaciones). Mantener una dieta antiinflamatoria y vigilar síntomas articulares.'},
            'TT': {'result': 'Mayor susceptibilidad a patologías autoinmunes', 'emoji': '🩺', 'detail': 'Dos alelos T. Mayor reactividad inmunitaria. Consultar con un médico especialista si aparecen dolores articulares persistentes o fatiga crónica.'},
        },
        'fun_fact': 'Es uno de los genes más fuertemente asociados a la autoinmunidad descubiertos en la era genómica. Su frecuencia en Europa del Norte ronda el 10-15%. ❄️'
    },

    'rs11136000': {
        'rsid': 'rs11136000',
        'gene': 'CLU',
        'category': 'Salud',
        'subcategory': 'Salud cognitiva',
        'title': 'Clusterina y aclaramiento amiloide cerebral (CLU)',
        'description': (
            'La clusterina (apolipoproteína J) es una chaperona molecular encargada de limpiar las proteínas amiloides tóxicas en el cerebro. '
            'Estudios GWAS masivos confirmaron que el alelo C de rs11136000 protege contra el deterioro cognitivo tardío.'
        ),
        'interpretations': {
            'TT': {'result': 'Riesgo cognitivo basal / estándar (CLU)', 'emoji': '🧠', 'detail': 'Función de clusterina normal. Riesgo cognitivo promedio poblacional en este locus.'},
            'CT': {'result': 'Protección parcial en aclaramiento cerebral', 'emoji': '🌟', 'detail': 'Un alelo C protector. Mayor eficacia en la eliminación de agregados proteicos cerebrales.'},
            'CC': {'result': 'Protección genética aumentada (CLU)', 'emoji': '🛡️', 'detail': 'Dos alelos C protectores. Asociado a menor riesgo de deterioro cognitivo tardío en estudios internacionales.'},
        },
        'fun_fact': 'El sistema glinfático del cerebro limpia los agregados amiloides principalmente durante las fases de sueño profundo. ¡Dormir 7-8 horas de calidad es la mejor neuroprotección! 💤'
    },

    'rs9939609': {
        'rsid': 'rs9939609',
        'gene': 'FTO',
        'category': 'Salud',
        'subcategory': 'Peso corporal',
        'title': 'Regulación del apetito y saciedad (FTO principal)',
        'description': (
            'El gen FTO (Fat Mass and Obesity-Associated) es el locus más influyente en la masa grasa corporal en humanos. '
            'El alelo A altera los circuitos hipotalámicos de la saciedad, produciendo mayor respuesta ante estímulos visuales de comida '
            'y menor sensación de plenitud gástrica tras comer.'
        ),
        'interpretations': {
            'TT': {'result': 'Saciedad normal / Menor propensión a sobrepeso', 'emoji': '✅', 'detail': 'Respuesta estándar a la saciedad. Menor tendencia genética a acumular tejido adiposo.'},
            'AT': {'result': 'Propensión moderada a menor saciedad', 'emoji': '⚖️', 'detail': 'Un alelo A. Ligera tendencia a requerir porciones más abundantes para saciarse. Dietas con alta densidad de fibra y proteína son muy efectivas.'},
            'AA': {'result': 'Mayor dificultad de saciedad (FTO)', 'emoji': '⚠️', 'detail': 'Dos alelos A (+3 kg de promedio si no se vigila el estilo de vida). El ejercicio aeróbico regular neutraliza por completo este efecto genético.'},
        },
        'fun_fact': 'Los portadores del alelo A tienen exactamente la misma capacidad de perder peso mediante dieta y ejercicio que los portadores de alelos protectores. ¡La genética no impide perder grasa! 🏃'
    },

}


def get_snp_info(rsid: str) -> dict | None:
    """
    Obtiene la información de un SNP por su rsID.

    Parameters
    ----------
    rsid : str
        Identificador del SNP (e.g., 'rs12913832').

    Returns
    -------
    dict | None
        Diccionario con la información del SNP, o None si no se encuentra.
    """
    return SNP_DATABASE.get(rsid.lower().strip())


def get_all_rsids() -> list:
    """Retorna la lista de todos los rsIDs en la base de datos."""
    return list(SNP_DATABASE.keys())


def get_snps_by_category(category: str) -> list:
    """
    Retorna todos los SNPs de una categoría específica.

    Parameters
    ----------
    category : str
        Categoría: 'Rasgo', 'Salud', 'Metabolismo', 'Ancestría'
    """
    return [
        info for info in SNP_DATABASE.values()
        if info.get('category', '').lower() == category.lower()
    ]


def get_interpretation(rsid: str, genotype: str) -> dict | None:
    """
    Obtiene la interpretación para un SNP y genotipo específicos.

    Parameters
    ----------
    rsid : str
        Identificador del SNP.
    genotype : str
        Genotipo del usuario (e.g., 'AG', 'GG').

    Returns
    -------
    dict | None
        Diccionario de interpretación o None si no se encuentra.
    """
    snp = get_snp_info(rsid)
    if not snp:
        return None

    interps = snp.get('interpretations', {})
    genotype = genotype.upper().strip()

    # Buscar directamente
    if genotype in interps:
        return interps[genotype]

    # Buscar genotipo revertido (e.g., AG -> GA)
    reversed_gt = genotype[::-1]
    if reversed_gt in interps:
        return interps[reversed_gt]

    return None


CATEGORY_ICONS = {
    'Rasgo': '🎨',
    'Salud': '❤️',
    'Metabolismo': '⚗️',
    'Ancestría': '🌍',
}

CATEGORY_COLORS = {
    'Rasgo': '#4CAF50',
    'Salud': '#F44336',
    'Metabolismo': '#FF9800',
    'Ancestría': '#2196F3',
}
