# Lab Semana 1 - Communities and Crime

- Persona A: Nataly Cuichan
- Persona B: Edwin Ortega
- Dataset: <[archive.ics.uci.edu/static/public/183/data.csv](https://archive.ics.uci.edu/static/public/183/data.csv)>
- Tarea: Regresion.
- Variable objetivo: ViolentCrimesPerPop

## Como correr
uv sync
uv run pytest -q
uv run python main.py

## Hallazgos
- **Persona A:** Revisando el dataset original, notamos que hay variables (sobre todo las relacionadas con la policía) que tienen más del 80% de datos en blanco. Por otro lado, la variable que queremos predecir (`ViolentCrimesPerPop`) tiene un formato numérico entre 0 y 1, así que no la escalamos.
- **Persona B:** Corrimos el análisis de correlación y confirmamos que las comunidades con un alto porcentaje de desempleo muestran una correlación lineal positiva muy clara con los crímenes violentos. La recta de mínimos cuadrados nos dio una pendiente de 0.58 y un intercepto de 0.02.

## Decisiones de limpieza
- Se eliminaron las columnas que presentaban más del 50% de valores nulos, ya que imputar una cantidad tan grande de datos introduciría un sesgo significativo en nuestro análisis.
- Las variables que tenían pocos nulos (que venían como un '?') los reemplazamos por el promedio (mean) de su columna.
- Normalizamos los nombres de algunas columnas para que sea más amigable programar.

## Pregunta de investigacion 1
**¿Por qué el comando `uv sync` garantiza que el proyecto sea reproducible en otra computadora?**
Porque usa el archivo `uv.lock` que nosotros subimos a GitHub. Ese archivo guarda las versiones exactas de cada paquete que instalamos en nuestras máquinas, así que cuando alguien más corre el comando, `uv` lee ese candado y le instala exactamente el mismo entorno sin que haya errores de versiones incompatibles.

## Pregunta de investigación 2
**¿Cuál es la diferencia entre correr `pytest` a secas y `uv run pytest`?**
- `pytest` a secas: Requiere que el entorno virtual esté activado manualmente antes de ejecutarlo. Si no se activa, Python intentará usar las librerías globales del sistema, lo que probablemente causará errores por dependencias faltantes.
- `uv run pytest`: Es más seguro. Automáticamente busca el entorno virtual del proyecto (guiándose por el `uv.lock`) y corre las pruebas ahí adentro, aunque tú no hayas activado nada a mano.
