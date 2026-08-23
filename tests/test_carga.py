import pandas as pd
from src import carga

def test_cargar():
    url = "https://archive.ics.uci.edu/static/public/183/data.csv"
    df = carga.cargar(url)
    assert isinstance(df, pd.DataFrame)
    assert not df.empty

def test_reporte_nulos():
    url = "https://archive.ics.uci.edu/static/public/183/data.csv"
    df = carga.cargar(url)
    reporte = carga.reporte_nulos(df)
    assert "columna" in reporte.columns
    assert "nulos" in reporte.columns
    assert "porcentaje" in reporte.columns

def test_guardar(tmp_path):
    url = "https://archive.ics.uci.edu/static/public/183/data.csv"
    df = carga.cargar(url)
    ruta = tmp_path / "limpio.parquet"
    carga.guardar(df, ruta)
    assert ruta.exists()