import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np

file_path= 'Apple_CA_Stats.xlsx'

#1er graph
df = pd.read_excel(file_path, sheet_name = 'Chiffres daffaire')


plt.figure(figsize=(10, 6))
plt.plot(df['Année'], df['Chiffres daffaires (milliards de Dollars)'], marker='o', linestyle='-', color='#dae025')
plt.title("Évolution du chiffre d'affaires d'Apple au fil des Années (en Milliards)")
plt.xlabel("Année")
plt.ylabel("CA")
plt.grid(True)
plt.tight_layout()

for i in range(len(df)):
    plt.text(df['Année'][i], df['Chiffres daffaires (milliards de Dollars)'][i] + 10,  
             str(df['Chiffres daffaires (milliards de Dollars)'][i]),  
             ha='center', fontsize=9, color='black') 

#2ème graph
df = pd.read_excel(file_path, sheet_name= 'Chiffres d\'Affaire par Région')

année =df['Année']
région1 = df['Amériques']
région2 = df['Europe']
région3 = df['Chine']
région4 = df['Japon']
région5 = df['Reste de l\'Asie-Pacifique']

bar_width = 0.2  
x = np.arange(len(année))  

plt.figure(figsize=(10, 6)) 

plt.bar(x - 2 * bar_width, région1, width=bar_width, label='Amérique', color='#dae033')
plt.bar(x - bar_width, région2, width=bar_width, label='Europe', color='#12233f')
plt.bar(x, région3, width=bar_width, label='Chine', color='#3f5371')
plt.bar(x + bar_width, région4, width=bar_width, label='Japon', color='#5a8c8b')
plt.bar(x + 2 * bar_width, région5, width=bar_width, label='Reste Asie-Pacifique', color='#37a8a4')

plt.xlabel("Année")  
plt.ylabel("CA") 
plt.title("Chiffre d'affaires par Région")
plt.xticks(x, année)  
plt.legend()
plt.tight_layout()

plt.show()


