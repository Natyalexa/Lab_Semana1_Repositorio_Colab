import numpy as np
import pandas as pd


def cargar(url, na_values=None):

    if na_values is None:
        na_values = ["?"]
    return pd.read_csv(url, na_values=na_values)

def reporte_nulos(df):
    """
    Devuelve un DataFrame con conteo y porcentaje de nulos por columna.
    """
    reporte = df.isnull().sum().reset_index()
    reporte.columns = ["columna", "nulos"]
    reporte["porcentaje"] = reporte["nulos"] / len(df) * 100
    return reporte.sort_values(by="nulos", ascending=False)

def limpiar(df):
    df = df.replace([np.inf, -np.inf], np.nan)
    df = df.drop_duplicates()

    for col in df.select_dtypes(include="object").columns:
        df[col] = df[col].str.strip().str.lower()
    df = df.reset_index(drop=True)
    return df

def guardar(df, ruta):
    df.to_parquet(ruta, index=False)

if __name__ == "__main__":
    url = "https://archive.ics.uci.edu/static/public/183/data.csv"
    df = cargar(url)
    print("Reporte de nulos inicial:")
    print(reporte_nulos(df).head(10))
    df_limpio = limpiar(df)
    guardar(df_limpio, "data/limpio.parquet")