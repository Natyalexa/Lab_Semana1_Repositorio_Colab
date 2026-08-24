import matplotlib.pyplot as plt
from src.carga import cargar, limpiar, reporte_nulos
from src.lab_semana1.analisis import resumen_por_grupo, top_k, recta_minimos_cuadrados

def main():
    print("--- 1. Reporte de Nulos (Dataset Crudo) ---")
    df_crudo = cargar("https://archive.ics.uci.edu/static/public/183/data.csv") # Ajusta la ruta si es diferente
    print(reporte_nulos(df_crudo))

    print("\n--- Limpiando Datos ---")
    df_limpio = limpiar(df_crudo)

    print("\n--- 2. Resumen por Grupo ---")
    # Cambiamos 'estado' por 'state' que es el nombre real de la columna
    resumen = resumen_por_grupo(df_limpio, 'state', ['ViolentCrimesPerPop'])
    print(resumen.head()) # Le agregué .head() para que no imprima una lista interminable

    print("\n--- 3. Top K (k=5) ---")
    top5 = top_k(df_limpio, 'ViolentCrimesPerPop', 5)
    print(top5)

    print("\n--- 4. Recta de Mínimos Cuadrados ---")
    # Elige dos columnas numéricas (ej. Desempleo vs Crímenes)
    x = df_limpio['PctUnemployed'].to_numpy()
    y = df_limpio['ViolentCrimesPerPop'].to_numpy()
    a, b = recta_minimos_cuadrados(x, y)
    print(f"Pendiente (a): {a}, Intercepto (b): {b}")

    print("\n--- 5. Gráfico Final ---")
    plt.scatter(x, y)
    plt.plot(x, a*x + b, color='red')
    plt.savefig("figura.png")
    print("Gráfico guardado como 'figura.png'")

# Corregidos los guiones bajos (son dos de cada lado: __name__ y __main__)
if __name__ == "__main__":
    main()