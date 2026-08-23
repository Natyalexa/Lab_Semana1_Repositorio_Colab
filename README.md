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
Observamos que las comunidades con un alto porcentaje de desempleo muestran una correlación lineal positiva muy fuerte con la variable de ViolentCrimesPerPop.
## Decisiones de limpieza
## Pregunta de investigacion 1
Funciona gracias al archivo uv.lock que se subio a GitHub. Ese archivo guarda los nombres y las versiones exactas de todos los paquetes que se instalo, por lo que uv sync solo lo lee y recrea el entorno igual en cualquier máquina