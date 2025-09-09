import pandas as pd 
#etraer datos
df=pd.read_csv("usuarios_app_limpieza.csv")
#mostrar primeros datos
print(df.head(2))
#ver info
print(df.info())
#descripcion general de los datos
print(df.describe())
#borrar duplicados
delete=df.drop_duplicates(subset=['usuario id','nombre','edad','país','tiempo sesión','estado'])
#llenar los espacio vacios con promedi
df['edad']=df['edad'].fillna(df['edad'].mean())
#filtrar por algo
usuarios_actio=df[df['estado']=='activo']
print(usuarios_actio)
