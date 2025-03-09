import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

file_path = 'Tesla_Stats.xlsx'

#1er Graph
df = pd.read_excel(file_path, sheet_name='Production')

plt.figure(figsize=(10, 6))
plt.bar(df['Année'], df['Production de voiture'], color='#e51837')

plt.title("Production Annuelle des Voitures Tesla")
plt.xlabel("Année")
plt.ylabel("Nombre de Voitures")
plt.grid(axis='y', linestyle='--', alpha=0.7) 


for i in range(len(df)):
    plt.text(df['Année'][i], df['Production de voiture'][i] + 5000, 
             str(df['Production de voiture'][i]),  
             ha='center', fontsize=9, color='black')

#2ème Graph
df = pd.read_excel(file_path, sheet_name = 'Ventes')


plt.figure(figsize=(10, 6))
plt.plot(df['Année'], df['Ventes'], marker='o', linestyle='-', color='#e51837')
plt.title("Ventes de Voitures Tesla par Année")
plt.xlabel("Année")
plt.ylabel("Ventes")
plt.grid(True)
plt.tight_layout()

for i in range(len(df)):
    plt.text(df['Année'][i], df['Ventes'][i] + 10,  
             str(df['Ventes'][i]),  
             ha='center', fontsize=9, color='black') 
    
#3ème Graph
df = pd.read_excel(file_path, sheet_name='Feuil3')

labels = df['Segment']
values = df['Recettes']

plt.title('Revenus par Secteur de Tesla')
plt.figure(figsize=(10, 6))
plt.pie(values, labels= labels, autopct='%1.1f%%', startangle=140,
        colors=['#e51837', '#e53a4f', '#e57e7f', '#e5a097'], 
        wedgeprops={'edgecolor': 'black'})

plt.show()