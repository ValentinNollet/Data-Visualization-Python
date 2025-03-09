import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

file_path = 'Kobe_vs_Jordan_Stats.xlsx'

df = pd.read_excel(file_path, sheet_name='Total Stats')

df.columns = df.columns.str.strip()

df['Joueurs'] = df['Joueurs'].str.strip()

joueur = df['Joueurs']
s0 = df['Nombre de Matchs']
s1 = df['Total des Points']
s2 = df['Total des Rebonds']
s3 = df['Total des passes décisives']
s4 = df['Total des Vols']
s5 = df['Total des Blocs']


bar_width = 0.2  
x = np.arange(len(joueur))  

plt.figure(figsize=(10, 6)) 


plt.bar(x - 2 * bar_width, s0, width=bar_width, label='Nombre de Matchs', color='#0167f8')
plt.bar(x - 2 * bar_width, s1, width=bar_width, label='Total des Points', color='#1d74e4')
plt.bar(x - bar_width, s2, width=bar_width, label='Total des Rebonds', color='#3982d1')
plt.bar(x, s3, width=bar_width, label='Total des passes décisives', color='#568fbd')
plt.bar(x + bar_width, s4, width=bar_width, label='Total des Vols', color='#729da9')
plt.bar(x + 2 * bar_width, s5, width=bar_width, label='Total des Blocs', color='#8eaa96')


plt.title("Comparaison Kobe VS Jordan : All Time Stats")
plt.xticks(x, joueur)  
plt.legend()
plt.tight_layout()


plt.show()

