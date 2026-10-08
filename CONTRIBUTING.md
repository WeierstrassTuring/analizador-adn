# Contribuir al proyecto ADN Personal

¡Las contribuciones son bienvenidas! Aquí te explicamos cómo ayudar.

## 🧬 Formas de contribuir

### Añadir nuevos SNPs a la base de datos
El archivo principal es `src/snp_database.py`. Para añadir un SNP:

1. Busca el rsID en [SNPedia](https://www.snpedia.com/) o [dbSNP](https://www.ncbi.nlm.nih.gov/snp/)
2. Verifica que está en el chip MyHeritage GSA (build37)
3. Añade la entrada al diccionario `SNP_DATABASE` siguiendo el formato existente
4. **Todo el texto debe estar en español**
5. Incluye siempre la fuente científica en el `fun_fact`

### Añadir ancestros famosos
El archivo es `src/famous_ancestors.py`. Para añadir un personaje histórico:

1. Verifica que hay evidencia genética (ADN antiguo) o alta probabilidad estadística
2. Incluye siempre la fuente científica en el campo `source`
3. Sé honesto con el nivel de `confidence`
4. Usa lenguaje en español

## ⚠️ Reglas importantes

- **NUNCA** subas archivos de ADN reales (el .gitignore los excluye, pero verifica)
- Las interpretaciones médicas deben ser **conservadoras y educativas**
- Incluye siempre fuentes científicas verificables
- Mantén el tono: informativo, curioso y accesible (no clínico ni alarmista)

## 🔧 Proceso de contribución

1. Fork del repositorio
2. Crea una rama: `git checkout -b feature/nuevo-snp`
3. Haz tus cambios
4. Ejecuta la app para verificar que funciona
5. Abre un Pull Request con descripción de los cambios

## 📋 Checklist para PRs

- [ ] El código funciona sin errores
- [ ] Los textos están en español
- [ ] Se incluyen fuentes científicas
- [ ] No se han subido datos de ADN
- [ ] Se ha actualizado el README si corresponde

