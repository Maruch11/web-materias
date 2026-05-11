# Contribuir al proyecto

Gracias por querer contribuir a `web-materias`. Este documento describe el flujo básico de colaboración.

## Flujo recomendado

1. Crear una rama nueva basada en `main`.
   - Nombre sugerido: `feature/<descripcion>`, `fix/<descripcion>`, `docs/<descripcion>`.
2. Hacer cambios en la rama.
3. Asegurarse de que los datos y la documentación estén actualizados.
4. Abrir un Pull Request contra `main`.

## Tipos de contribución

- `data/`: cambios en los archivos de datos.
- `README.md`, `data/README.md`: mejoras de documentación.
- `.github/`: plantillas de issues y PR.

## Regla de datos

- Mantener los datos en `data/careers.csv` y `data/subjects.csv`.
- No editar el archivo binario de Xojo sin documentarlo claramente.
- Si se agrega una nueva carrera o materia, actualizar solo el CSV correspondiente.

## Good practices

- Escribir un mensaje de commit con conventional commit en inglés.
- Incluir en el PR una descripción breve de los cambios.
- Si el cambio es en datos, explicar qué se agregó o se normalizó.

## Archivos útiles

- `data/README.md`: explica el esquema de los CSV.
- `scripts/validate_csv.py`: valida columnas y consistencia básica.
- `.github/ISSUE_TEMPLATE.md`: plantilla para reportar problemas.
- `.github/pull_request_template.md`: plantilla para describir cambios.
- `xojo-current-logic.md` : documentacion manual de eventos, metodos, pproiedades, etc.