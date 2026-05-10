# Datos del proyecto

Este directorio contiene los archivos de datos que alimentan la aplicación.

## Archivos

- `careers.csv`: lista de carreras.
- `subjects.csv`: lista de materias asociadas a cada carrera.

## Esquema de `data/careers.csv`

```csv
career_id,career_name,career_slug
```

- `career_id`: identificador numérico único.
- `career_name`: nombre visible de la carrera.
- `career_slug`: identificador legible en URLs o filtros internos.

## Esquema de `data/subjects.csv`

```csv
subject_id,career_id,subject_name,term,official_url,notes,starts
```

- `subject_id`: identificador numérico único.
- `career_id`: referencia a `career_id` en `data/careers.csv`.
- `subject_name`: nombre de la materia.
- `term`: periodo o cuatrimestre (p. ej. `Anual`, `1° cuatrimestre`).
- `official_url`: enlace al manual, recurso o GPT.
- `notes`: observaciones opcionales.
- `starts`: indicador de inicio o metadata adicional.

## Reglas básicas

- La relación entre carreras y materias se hace con `career_id`.
- No se deben duplicar `subject_id` ni `career_id`.
- `official_url` puede quedar vacío cuando aún no existe recurso asociado.
- `term` debe mantenerse consistente entre registros.

## Notas

Las columnas `link_raw` y `manual_raw` pueden existir como datos heredados, pero el modelo canónico del proyecto debería usar `official_url`.
