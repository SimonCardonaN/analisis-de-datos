import matplotlib.pyplot as plt
import pandas as pd 
import seaborn as sns 
#leer archivo
df=pd.read_csv("usuarios_app_limpieza.csv")
#que va a graficar 
df['pais'].value_counts().plot(kind='bar')
#decoracion
plt.title("Usuarios por pais")
plt.xlabel('pais')
plt.ylabel('cantidad de usuarios')
plt.show()
