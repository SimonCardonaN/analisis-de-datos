import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns 
df=pd.read_csv("usuarios_app_limpieza.csv")
#limpieza de edad 
df.drop_duplicates()
df=df.dropna(subset=['edad'])
#conteos=df['pais'].value_counts()
#colors=sns.color_palette("pastel",len(conteos))

plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='pais', y='edad', palette='pastel')
plt.title("cantidad de usuarios por pais") 
plt.xlabel('pais') 
plt.ylabel('edad')
plt.show()