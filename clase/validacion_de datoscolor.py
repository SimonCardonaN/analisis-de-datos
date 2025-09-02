import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
df=pd.read_csv("usuarios_app_limpieza.csv")
#contar los paises que hay
conteos=df['pais'].value_counts()
colors=sns.color_palette("pastel",len(conteos))
mostrar=conteos.plot(kind="bar",color=colors)
plt.title("cantidad de usuarios por pais")
plt.xlabel('pais')
plt.ylabel('cantidad de usuarios')
plt.show()