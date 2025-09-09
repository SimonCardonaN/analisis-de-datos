import pandas as pd
import numpy as np
import re as er

# 1) Leer el archivo
df = pd.read_csv("usuarios_app_clase2.csv", encoding="utf-8")

# Normalizar columnas
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_", regex=False)

# Diccionario de país
map_pais = {
    "méxico": "México",
    "mexico": "México",
    "Mexico": "México"
}

# 2) Arreglar valores mal escritos en la columna 'pais'
df['pais'] = df['pais'].astype(str).str.strip().replace(map_pais)

# Función para convertir texto a número
def to_number(x):
    if pd.isna(x) or str(x).strip() == "":
        return np.nan
    s = str(x).strip().lower()
    palabra = {
        "quince": 15,
        "diez": 10,
        "veinte": 20,
        "cien": 100
        # Agrega más si es necesario
    }
    if s in palabra:
        return float(palabra[s])
    m = er.search(r"(\d+)", s)
    return float(m.group(1)) if m else np.nan

# Aplicar función
df['edad'] = df['edad'].apply(to_number)
df['tiempo_sesion_min'] = df['tiempo_sesion_min'].apply(to_number)

# Validar que sean numéricos
df['clicks'] = pd.to_numeric(df['clicks'], errors="coerce")
df['compras'] = pd.to_numeric(df['compras'], errors="coerce")

# Eliminar duplicados ignorando id_cliente
df = df.drop_duplicates(subset=["nombre", "edad", "pais", "tiempo_sesion_min", "estado", "suscripcion", "clicks", "compras"])

# Quitar filas sin edad ni tiempo de sesión
df = df.dropna(subset=["edad", "tiempo_sesion_min"])

# Rango razonable
df = df[df['edad'].between(10, 100)]
df = df[df['tiempo_sesion_min'].between(0, 10000)]

# Guardar archivo limpio
df.to_csv("app_limpieza_normalizado.csv", index=False, encoding="utf-8")

print("Limpieza finalizada. Filas:", df.shape[0])
