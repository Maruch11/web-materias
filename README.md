# Materias y Manuales

Aplicación web desarrollada en **Xojo** para consultar materias por carrera y cuatrimestre, y acceder al manual, recurso o GPT asociado cuando exista.

## Objetivo

El objetivo del proyecto es construir una app simple que permita:

1. seleccionar una carrera;
2. seleccionar un período o cuatrimestre;
3. listar las materias correspondientes;
4. acceder al manual, enlace o GPT asociado a cada materia.

## Estado actual

El proyecto se encuentra en etapa inicial/prototipo.

Actualmente cuenta con:

- proyecto Xojo Web iniciado;
- interfaz visual inicial;
- botones de selección de carrera;
- botones de selección de cuatrimestre;
- lista visual de materias;
- archivos CSV normalizados;
- documentación inicial del modelo de datos;
- repositorio Git iniciado.

## Estructura del proyecto

```text
web-materias/
├── .git/
├── careers.csv
├── subjects.csv
├── README.md
└── materias_y_manuales.xojo_binary_project
```

## Archivos principales

### `materias_y_manuales.xojo_binary_project`

Proyecto principal desarrollado en Xojo.

Contiene la interfaz web inicial de la aplicación.

### `careers.csv`

Archivo normalizado con las carreras disponibles.

Modelo esperado:

```text
career_id
career_name
career_slug
```

### `subjects.csv`

Archivo normalizado con las materias asociadas a cada carrera.

Modelo esperado:

```text
subject_id
career_id
subject_name
term
official_url
notes
starts
```

## Modelo de datos

### Tabla lógica: `careers`

Representa las carreras disponibles.

```text
id
name
slug
```

### Tabla lógica: `subjects`

Representa las materias asociadas a cada carrera.

```text
id
career_id
name
term
official_url
notes
starts
```

## Mapeo de datos

### Fuente original

El dataset original contenía campos como:

```text
Policia/Bomberos
Anual/Cuatrimestre
Materia
Link
Manual
Obs
inicia
```

### Modelo normalizado

El modelo normalizado separa carreras y materias.

```text
Policia/Bomberos      → careers
Materia               → subjects.name
Anual/Cuatrimestre    → subjects.term
Link/Manual           → subjects.official_url
Obs                   → subjects.notes
inicia                → subjects.starts
```

## Reglas de normalización

- Cada carrera se guarda una sola vez en `careers.csv`.
- Cada materia se guarda en `subjects.csv`.
- Cada materia referencia una carrera mediante `career_id`.
- Los IDs de los CSV funcionan como seed inicial.
- Los enlaces pueden estar vacíos si todavía no existe manual o GPT asociado.
- Los valores de `term` deben mantenerse consistentes.

Ejemplos recomendados para `term`:

```text
Anual
1° cuatrimestre
2° cuatrimestre
3° cuatrimestre
4° cuatrimestre
```

## Flujo esperado de la aplicación

```text
Usuario selecciona carrera
        ↓
Usuario selecciona cuatrimestre
        ↓
La app filtra subjects.csv
        ↓
La lista muestra materias reales
        ↓
Usuario selecciona una materia
        ↓
La app abre el recurso asociado si existe
```

## Comportamiento esperado

### Si la materia tiene enlace

La aplicación debe abrir el valor de `official_url`.

### Si la materia no tiene enlace

La aplicación debe mostrar un aviso, por ejemplo:

```text
Manual o GPT aún no cargado para esta materia.
```

## Funcionalidades actuales

- Interfaz inicial en Xojo Web.
- Selección visual de carrera.
- Selección visual de cuatrimestre.
- Lista de materias.
- Botón para acceder a un recurso externo.

## Funcionalidades pendientes

- Cargar carreras desde `careers.csv`.
- Cargar materias desde `subjects.csv`.
- Reemplazar materias hardcodeadas.
- Filtrar materias por carrera.
- Filtrar materias por cuatrimestre.
- Asociar cada fila de la lista con su `official_url`.
- Validar enlaces vacíos.
- Mostrar mensajes claros al usuario.
- Mejorar textos visibles de la interfaz.
- Documentar el flujo implementado.

## Próximo hito

Conectar la interfaz Xojo con los CSV normalizados.

### Resultado esperado del hito

```text
Selecciono Policía
Selecciono 1° cuatrimestre
Veo solo las materias correspondientes
Selecciono una materia
Abro su manual/GPT si existe
```

## Alcance actual

Este proyecto apunta a una demo funcional simple.

Incluye:

- lectura de datos;
- filtrado;
- visualización;
- acceso a recursos externos.

No incluye todavía:

- login de usuarios;
- base de datos productiva;
- ABM completo;
- edición desde interfaz;
- deploy productivo;
- administración de permisos.

## Posible evolución futura

Una vez validada la demo inicial, el proyecto puede evolucionar hacia:

- uso de SQLite local;
- - integración con una base de datos institucional, a definir con Infraestructura/DBA;
- panel de administración;
- carga y edición de materias;
- asociación de múltiples recursos por materia;
- búsqueda por texto;
- filtros avanzados;
- despliegue web.

## Decisión pendiente de infraestructura

La persistencia definitiva de datos y el almacenamiento de manuales quedan sujetos a validación con el área de Infraestructura/DBA.

Aspectos a definir:

- motor de base de datos recomendado;
- modalidad de conexión desde Xojo;
- ubicación definitiva de los manuales;
- permisos de acceso;
- backups;
- mantenimiento;
- despliegue interno o externo.

## Nota sobre Xojo

El proyecto se encuentra guardado como archivo binario de Xojo:

```text
materias_y_manuales.xojo_binary_project
```

Este formato es válido para trabajar desde el IDE, aunque no es el más cómodo para revisar cambios en Git.

Más adelante podría evaluarse guardar el proyecto en un formato textual de Xojo para mejorar el versionado.

## Estado del proyecto

```text
Prototipo encaminado
```

La prioridad actual es consolidar la carga de datos reales desde los CSV y reemplazar los valores de prueba en la interfaz.
