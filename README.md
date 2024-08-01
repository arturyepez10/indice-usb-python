# Indice USB

#### Autor
- Arturo Yepez

## Descripción

El actual repositorio tiene como objetivo el ser una herramienta con la que poder hacer cálculo del **Indice Academico** para los estudiantes de la Universidad Simón Bolívar en Caracas, Venezuela.

Este se define como una medida cuantitativa que refleja el rendimiento académico de un estudiante. Este índice se calcula en función de las calificaciones obtenidas en las asignaturas cursadas y los créditos asociados a cada una.

Una de las características del **Indice Academico** es que ofrece una visión clara del desempeño académico del estudiante a lo largo de su carrera universitaria.

## Calculo del Indice Academico

El cálculo del índice académico se realiza de la siguiente manera:
1. **Calificación ponderada de cada asignatura**: Se multiplica la calificación obtenida en cada asignatura por el número de créditos de esa asignatura.
1. **Suma de las calificaciones ponderadas**: Se suman todas las calificaciones ponderadas.
1. **Suma de los créditos**: Se suman los créditos de todas las asignaturas cursadas.
1. **Cálculo del índice académico**: Se divide la suma de las calificaciones ponderadas entre la suma de los créditos.

La fórmula es:

$$
\text{Índice Académico} = \frac{\sum (\text{Calificación de la asignatura} \times \text{Créditos de la asignatura})}{\sum (\text{Créditos de las asignaturas})}
$$

Para estos cálculos:
- No se considerarán las asignatura que tienen "Nota sin efecto" o "Retirada"
- Este indice tiene carácter acumulativo y se calcula trimestralmente tomando en cuenta todas las asignaturas cursadas desde el primer período academico en la universidad.

### Notas sin Efecto

Significa que si apruebas una asignatura anteriormente aplazada, la nueva calificación aprobatoria anulará la nota inmediata para el cálculo del índice académico. Ambas calificaciones se harán constar en tu expediente, y adicionalmente se colocará el calificativo "Nota sin Efecto" a la calificación anterior.

Cabe destacar, si una asignatura es reprobada más de 2 veces, la "Nota sin Efecto" solo se aplica a la última instancia antes de aprobarse.

### Asignatura Retirada

Es un proceso donde los estudiantes pueden abandonar una asignatura sin que afecte negativamente su índice académico. A la asignatura retirada se le agrega el calificativo de "Retirada" y en la nota se coloca un "R".

Entre las características 

## Instalación

La librería funciona con los paquetes nativos de Python, por lo que no se requiere instalación de ninguna librería extra.

## Uso

Usar esta herramienta es muy sencillo, en su version actual (*v1.0*) solo requiere de seguir los siguientes pasos:

1. En el repositorio, se encuentra un template *template.xlxs* con un formato especial (que será explicado con detalle más adelante).
1. Llenar el template con la información de todos los períodos académicos del estudiante (como se marca en la página del Expediente Académico).
1. Exportar la hoja de cálculo a `*.csv` (Formato CSV) donde las columnas figuren en la primera fila.
1. Correr el proyecto con el siguiente comando:
```bash
python main.py -n {{ NOMBRE }}
```
Donde `{{ NOMBRE }}` debe ser reemplazado por el nombre del archivo generado y exportado a CSV (incluyendo la extensión). En caso de no existir o pasar por parametro el nombre, se asume que el nombre del archivo es `expediente.csv`.

### Plantilla 

La plantilla a llenarse contiene las siguientes columnas con los siguientes formatos (en ese orden específico):
1. No. de Trimestre -> `número entero`
1. Codigo de Materia -> `string`
1. Nombre de Materia -> `string`
1. Creditos -> `número entero`
1. Nota -> `número entero`
1. Comentarios -> `<select> [ N/A, Retirada, Sin Efecto ]`

Es de suma importancia los siguientes puntos:
* El orden establecido para las columnas, **en caso de cambiarlo, no se garantiza el resultado obtenido**.
* El valor de "*Observaciones*" puede ser no necesariamente "N/A" pero es importante que en los casos correspondientes el valor de esa casilla sea "*Retirada*" o "*Sin Efecto*"

El template también puede conseguirse en el siguiente enlace: [template](https://docs.google.com/spreadsheets/d/1qaVOB9BGMAlpHmo-S8KdfMH_NoQyfcPL/edit?usp=share_link&ouid=116169802522762914319&rtpof=true&sd=true). Se puede descargar y así utilizar desde la raíz del proyecto.

## Futura Mejoras

Se preveen algunas iteraciones extras para mejorar las funcionalidades disponibles. Entre esos cambios, se trabaja en lo siguiente:

1. **Capacidad de mostrar el índice acumulado por período académico.** Actualmente solo se muestra el indice actual y el indice individual de cada uno de los períodos.
1. **Conversión automática de hojas de cálculo** Actualmente hay que hacer la conversión a CSV, pero se prevee que en el futuro no sea necesario y lo haga el mismo proyecto.

## Sugerencias

Si tienen alguna sugerencia, sientanse libres de contactarme o crear un *issue* al respecto :)