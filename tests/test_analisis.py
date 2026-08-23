import numpy as np
import pandas as pd
import pytest

from src.lab_semana1.analisis import (
    filtrar,
    recta_minimos_cuadrados,
    resumen_por_grupo,
    top_k,
    zscore,
)


@pytest.fixture
def df_mini():
    """Datos de prueba reutilizables."""
    return pd.DataFrame({
        "grupo": ["a", "a", "b", "b"],
        "valor": [10.0, 20.0, 30.0, 40.0]
    })

def test_filtrar_deja_solo_los_mayores():
    df = pd.DataFrame({"edad": [10, 25, 40]})
    resultado = filtrar(df, "edad", 20)
    assert len(resultado) == 2
    assert resultado["edad"].min() > 20

def test_resumen_por_grupo_calcula_metricas(df_mini):
    r = resumen_por_grupo(df_mini, "grupo", ["valor"])
    assert r.loc["a", ("valor", "mean")] == 15.0
    assert r.loc["b", ("valor", "count")] == 2.0

def test_zscore_tiene_media_cero_y_desviacion_uno(df_mini):
    matriz = df_mini[["valor"]].to_numpy()
    z = zscore(matriz)
    assert np.mean(z) == pytest.approx(0.0, abs=1e-9)
    assert np.std(z, axis=0)[0] == pytest.approx(1.0, abs=1e-9)

def test_top_k_devuelve_los_mas_grandes(df_mini):
    resultado = top_k(df_mini, "valor", 2)
    assert len(resultado) == 2
    assert resultado.iloc[0]["valor"] == 40.0

def test_recta_minimos_cuadrados_ajuste_perfecto():
    # Puntos perfectamente alineados en la recta y = 2x + 1
    x = np.array([1.0, 2.0, 3.0])
    y = np.array([3.0, 5.0, 7.0])
    a, b = recta_minimos_cuadrados(x, y)
    assert a == pytest.approx(2.0)
    assert b == pytest.approx(1.0)