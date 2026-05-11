# Lógica actual del proyecto Xojo

Documento manual para describir la lógica visible del proyecto Xojo, ya que el archivo principal está en formato binario.

## Entorno

- Xojo 2025r3.1
- Proyecto: materias_y_manuales.xojo_binary_project
- Tipo: Xojo Web

## Estado actual

La aplicación funciona como prototipo y ya carga materias desde `data/subjects.csv` usando una ruta absoluta local durante el desarrollo.

## Estructura
```
App
Session
WebPage1
  Controls
    btnBombero
      Pressed
    btnCuatrimestre Set
      Event Handlers
        Pressed
      Members
        btnCuatrimestre(0)
        btnCuatrimestre(1)
        btnCuatrimestre(2)
        btnCuatrimestre(3)
    btnGPT
      Pressed
    btnPolicia
      Pressed
    ImageViewer1
    lblBienvenida
    lstMaterias
      Pressed
    Rectangle1

  Methods
    GoToURL
    mParseCSVLine
    mLlenarLista
    mTermSeleccionado

  Properties
    intCuatrimestre
    intTipo
    strOfficialURLSeleccionada
```
## Propiedades principales

### `intTipo`

Define la carrera seleccionada.

| Valor | Carrera |
|---:|---|
| 1 | Policía |
| 2 | Bombero |

### `intCuatrimestre`

Define el período seleccionado.

| Valor | Período |
|---:|---|
| 1 | 1° cuatrimestre |
| 2 | 2° cuatrimestre |
| 3 | 3° cuatrimestre |
| 4 | 4° cuatrimestre |

### `strOfficialURLSeleccionada`

Guarda la URL operativa (`official_url`) de la materia seleccionada en `lstMaterias`.

## Métodos actuales

### `mLlenarLista`

Lee `data/subjects.csv`, filtra materias por carrera y período, muestra los nombres en `lstMaterias` y guarda `official_url` en `RowTagAt`.

Actualmente usa una ruta absoluta local:

```xojo
C:\Users\mmazzoccoli\dev\web-materias\data\subjects.csv
```

Esta ruta sirve para desarrollo. Para empaquetar la app, falta mover el CSV a recursos/copied files o definir una ubicación definitiva.

### `mTermSeleccionado`

Convierte `intCuatrimestre` al valor usado en la columna `term` de `data/subjects.csv`.

Nota: el CSV actual mezcla formatos: `1° cuatrimestre`, `2° cuatrimestre`, `3` y `4`.

### `mParseCSVLine`

Parsea una línea CSV respetando comillas y comas internas.

### `GoToURL`

Método utilizado para abrir una URL externa.

## Eventos actuales
- `btnPolicia.Pressed`

Asigna la carrera Policía mediante intTipo = 1.

- `btnBombero.Pressed`

Asigna la carrera Bombero mediante intTipo = 2.

- `btnCuatrimestre.Pressed`

Asigna el período mediante intCuatrimestre.

- `lstMaterias.Pressed`

Guarda la URL real de la materia seleccionada desde `RowTagAt`.

- `btnGPT.Pressed`

Verifica que haya una materia seleccionada y abre `strOfficialURLSeleccionada`.

## Decisión de datos

La URL operativa sale de:

'official_url'

No deben usarse como fuente operativa:

'link_raw'
'manual_raw'

Estas columnas quedan como datos originales/provisorios.

## Código actual

- btnPolicia.Pressed
```xojo
intTipo = 1
lstMaterias.RemoveAllRows
me.Indicator = WebButton.Indicators.Danger
btnBombero.Indicator = WebButton.Indicators.Default
var i as integer
for i = 0 to 3
  btnCuatrimestre(i).Indicator = WebButton.Indicators.Default
next i
btnGPT.Indicator = WebButton.Indicators.Default
```

- btnBombero.Pressed
```xojo
intTipo = 2
lstMaterias.RemoveAllRows
me.Indicator = WebButton.Indicators.Danger
btnPolicia.Indicator = WebButton.Indicators.Default
var i as integer
for i = 0 to 3
  btnCuatrimestre(i).Indicator = WebButton.Indicators.Default
next i
btnGPT.Indicator = WebButton.Indicators.Default
```

- btnCuatrimestre.Pressed (set)
```xojo
intCuatrimestre = index + 1
var i as integer
for i = 0 to 3
  btnCuatrimestre(i).Indicator = WebButton.Indicators.Default
next i
me.Indicator = WebButton.Indicators.Danger
btnGPT.Indicator = WebButton.Indicators.Default
mLlenarLista
```

- lstMaterias.Pressed
```xojo
If lstMaterias.SelectedRowIndex = -1 Then
  strOfficialURLSeleccionada = ""
  btnGPT.Indicator = WebButton.Indicators.Default
  Return
End If

strOfficialURLSeleccionada = lstMaterias.RowTagAt(lstMaterias.SelectedRowIndex).StringValue
btnGPT.Indicator = WebButton.Indicators.Danger
```
- btnGPT.Pressed
```xojo
If lstMaterias.SelectedRowIndex = -1 Then
  MessageBox("Debe seleccionar una materia.")
  Return
End If

If strOfficialURLSeleccionada.Trim = "" Then
  MessageBox("Manual o GPT aún no cargado para esta materia.")
  Return
End If

GoToURL(strOfficialURLSeleccionada, True)
```
## Métodos
- mTermSeleccionado
```xojo
' Convierte el número de cuatrimestre seleccionado al texto usado en data/subjects.csv.

Select Case intCuatrimestre
Case 1
  Return "1° cuatrimestre"
Case 2
  Return "2° cuatrimestre"
Case 3
  Return "3"
Case 4
  Return "4"
End Select

Return ""
```

- mParseCSVLine
```xojo
' Lee una línea CSV respetando comillas y comas internas.

Var values() As String
Var current As String
Var insideQuotes As Boolean = False

For i As Integer = 0 To line.Length - 1
  Var ch As String = line.Middle(i, 1)
  
  If ch = """" Then
    If insideQuotes And i < line.Length - 1 And line.Middle(i + 1, 1) = """" Then
      current = current + """"
      i = i + 1
    Else
      insideQuotes = Not insideQuotes
    End If
    
  ElseIf ch = "," And Not insideQuotes Then
    values.Add(current)
    current = ""
    
  Else
    current = current + ch
  End If
Next

values.Add(current)
Return values
```

- mLlenarLista
```xojo
lstMaterias.RemoveAllRows
strOfficialURLSeleccionada = ""
btnGPT.Indicator = WebButton.Indicators.Default

Var selectedTerm As String = mTermSeleccionado()

Var csvFile As FolderItem = New FolderItem("C:\Users\mmazzoccoli\dev\web-materias\data\subjects.csv", FolderItem.PathModes.Native)

If Not csvFile.Exists Then
  MessageBox("No se encontró data/subjects.csv")
  Return
End If

Var input As TextInputStream = TextInputStream.Open(csvFile)
input.Encoding = Encodings.UTF8

If input.EndOfFile Then
  input.Close
  Return
End If

Var headerLine As String = input.ReadLine
Var headers() As String = mParseCSVLine(headerLine)

Var idxCareer As Integer = headers.IndexOf("career_id")
Var idxSubject As Integer = headers.IndexOf("subject_name")
Var idxTerm As Integer = headers.IndexOf("term")
Var idxOfficialURL As Integer = headers.IndexOf("official_url")

If idxCareer = -1 Or idxSubject = -1 Or idxTerm = -1 Or idxOfficialURL = -1 Then
  input.Close
  MessageBox("El CSV no tiene las columnas requeridas.")
  Return
End If

While Not input.EndOfFile
  Var line As String = input.ReadLine.Trim
  
  If line = "" Then Continue
  
  Var cols() As String = mParseCSVLine(line)
  
  If cols.LastIndex < idxOfficialURL Then Continue
  
  Var rowCareerId As Integer = cols(idxCareer).ToInteger
  Var rowSubject As String = cols(idxSubject)
  Var rowTerm As String = cols(idxTerm)
  Var rowOfficialURL As String = cols(idxOfficialURL)
  
  If rowCareerId = intTipo And (rowTerm = selectedTerm Or rowTerm = "Anual") Then
    lstMaterias.AddRow(rowSubject)
    lstMaterias.RowTagAt(lstMaterias.LastAddedRowIndex) = rowOfficialURL
  End If
Wend

input.Close
```

- GoToURL
```xojo
GoToURL (url As String, inNewWindow As Boolean = False)
// Calling the overridden superclass method.
Super.GoToURL(url, inNewWindow)
```

### Notes
-- Untitled
Tabla original con
Policia/Bombero
Cuatrimestre
Materia
Link
Manual

## Properties
-- IntCuatrimestre As Integer = 1
1 = 1 Cuatrimestre
2 = 2 Cuatrimestre
3 = 3 Cuatrimestre
4 = 4 Cuatrimestre
-- IntTipo As Integer = 1
1 = Policia
2 = Bombero
-- strOfficialURLSeleccionada As String
URL operativa de la materia seleccionada.

### Logo
Ubicación de archivo en carpeta documentos del disco local, hay que ubicar el archivo en el proyecto

## Próximo ajuste lógico

La carga desde CSV ya está implementada en el prototipo. Quedan como próximos ajustes:

- Reemplazar la ruta absoluta local por una ubicación empaquetable o configurable.
- Normalizar los valores de `term` en `data/subjects.csv`.
- Agregar `data/subjects.csv` como recurso/copied file si se mantiene `SpecialFolder.Resources`.
- Confirmar la ubicación definitiva del logo dentro del proyecto.
