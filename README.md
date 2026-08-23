# Lab Semana 1 - <Communities and Crime>
- Persona A: <Edwin Ortega>
- Persona B: <Nataly Cuichan>
- Dataset: <archive.ics.uci.edu/static/public/183/data.csv>
- Tarea: <regresion | clasificacion> Variable objetivo: <ViolentCrimesPerPop>
## Como correr
uv sync
uv run pytest -q
uv run python main.py
## Hallazgos
- Hallazgo de A: El dataset tiene valores faltantes en varias columnas. La variable objetivo `ViolentCrimesPerPop` está en formato numérico entre 0 y 1.
- Hallazgo de B: Observamos que las comunidades con un alto porcentaje de desempleo muestran una correlación lineal positiva muy fuerte con la variable de ViolentCrimesPerPop.
## Decisiones de limpieza
- Se eliminaron columnas con más del 50% de valores nulos.
- Se normalizaron nombres de columnas para facilitar el análisis.
## Pregunta de investigacion 1
Funciona gracias al archivo uv.lock que se subio a GitHub. Ese archivo guarda los nombres y las versiones exactas de todos los paquetes que se instalo, por lo que uv sync solo lo lee y recrea el entorno igual en cualquier máquina
## Pregunta de investigación 2
¿Cuál es la diferencia entre correr `pytest` a secas y `uv run pytest`?
- **pytest**: depende de que el usuario haya activado manualmente el entorno virtual. Si no lo hizo, las pruebas se ejecutan con el Python global del sistema y pueden fallar por falta de dependencias.
- **uv run pytest**: asegura que las pruebas se ejecuten dentro del entorno virtual gestionado por uv, con las dependencias correctas definidas en `uv.lock`. Esto evita errores aunque el usuario no haya activado el entorno.