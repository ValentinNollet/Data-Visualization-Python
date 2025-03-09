import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file_path = 'Messi_vs_Ronaldo_Stats.xlsx'


df = pd.read_excel(file_path, sheet_name='All time Stats sans USA SAUDI ')


df.columns = df.columns.str.strip()


df['Joueurs'] = df['Joueurs'].str.strip()

joueur = df['Joueurs']
s1 = df['Nombre de Matchs jouées']
s2 = df['Nombre de buts']
s3 = df['Nombre de passes décisives']
s4 = df['Penalty']
s5 = df['Free Kick']


bar_width = 0.2  
x = np.arange(len(joueur))  

plt.figure(figsize=(10, 6)) 


plt.bar(x - 2 * bar_width, s1, width=bar_width, label='Nombre de Matchs jouées', color='#4a6d42')
plt.bar(x - bar_width, s2, width=bar_width, label='Nombre de buts', color='#59764d')
plt.bar(x, s3, width=bar_width, label='Nombre de passes décisives', color='#697f58')
plt.bar(x + bar_width, s4, width=bar_width, label='Penalty', color='#788863')
plt.bar(x + 2 * bar_width, s5, width=bar_width, label='Free Kick', color='#88916e')


plt.title("Comparaison Messi Ronaldo : All Time Stats Without USA & SAUDI")
plt.xticks(x, joueur)  
plt.legend()
plt.tight_layout()


plt.show()