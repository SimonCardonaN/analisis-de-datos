import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar los datos
df = pd.read_csv(r"C:\Users\Multimedia\Documents\analisis de datos\app_limpieza_normalizado.csv", encoding="utf-8")

# Contar la cantidad de usuarios
total_usu = len(df)
print("CANTIDAD DE USUARIOS: ", total_usu)

# Agrupar por país y estado, calcular estadísticas
asorn = (
    df.groupby(["pais", "estado"])["tiempo_sesion_min"]
    .agg(["mean", "median", "count"])
    .rename(columns={"mean": "promedio", "median": "mediana", "count": "cantidad"})
    .reset_index()
)

# Mostrar resultado
print("Estadística por país y estado:")
print(asorn)
