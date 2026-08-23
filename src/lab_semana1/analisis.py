import numpy as np
import pandas as pd

def filtrar(df, columna, umbral):
    """Devuelve solo las filas donde df[columna] > umbral."""
    return df[df[columna] > umbral]

def resumen_por_grupo(df, col_grupo, cols_num):
    """Compara el comportamiento entre categorías."""
    return df.groupby(col_grupo)[cols_num].agg(['mean', 'std', 'count'])

def zscore(matriz):
    """Normaliza por columna usando broadcasting."""
    return (matriz - matriz.mean(axis=0)) / matriz.std(axis=0)

def top_k(df, columna, k):
    """Los k registros con mayor valor usando np.argsort."""
    # np.argsort ordena de menor a mayor, tomamos los últimos k y los invertimos
    indices = np.argsort(df[columna].values)[-k:][::-1]
    return df.iloc[indices]

def recta_minimos_cuadrados(x, y):
    """Ajusta una recta con minimos cuadrados y devuelve (a, b)."""
    # Matriz de diseño apilando x junto a una columna de unos
    matriz_diseno = np.vstack([x, np.ones(len(x))]).T
    a, b = np.linalg.lstsq(matriz_diseno, y, rcond=None)[0]
    return a, b