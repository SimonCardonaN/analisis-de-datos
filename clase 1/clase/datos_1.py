import pandas as pd
#leer datos
df=pd.read_csv("usuarios_app.csv")
#mostrar datos
print(df.head(2))
#ver informacion general
print(df.info())
#ver una descripcion de la tabla,promedios minimos maximos etc
print(df.describe())