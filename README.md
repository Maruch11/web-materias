## Data mapping

### Fuente → Modelo

CSV (origen):
- Policia/Bomberos
- Anual/Cuatrimestre
- Materia
- Link
- Manual
- Obs
- inicia

Modelo (Supabase):

careers
- id
- name
- slug

subjects
- id
- career_id (FK → careers.id)
- name
- term
- official_url
- notes
- starts

### Reglas
- Policia/Bomberos → careers.id
- Materia → subjects.name
- Anual/Cuatrimestre → subjects.term
- Link/Manual → subjects.official_url
- IDs del CSV son solo seed inicial
