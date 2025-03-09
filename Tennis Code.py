import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

file_path = 'Federer_vs_Nadal_Stats.xlsx'

#1er graph
df = pd.read_excel(file_path, sheet_name='Feuil1')

plt.figure(figsize=(10, 6 ))
plt.plot(df['Year'], df['Rank'], marker='o', linestyle='-', color='#0167f8')
plt.title('Ranking de Federer au Cours des Années')
plt.xlabel('Année')
plt.ylabel('Rank')

for i in range(len(df)):
    plt.text(df['Year'][i], df['Rank'][i] + 10,  
             str(df['Rank'][i]),  
             ha='center', fontsize=9, color='black')

#2ème graph
df = pd.read_excel(file_path, sheet_name='Feuil2')

plt.figure(figsize=(10, 6))
plt.plot(df['Year'], df['Rank'],marker='o', linestyle='-', color='#ffe047')
plt.title('Ranking de Nadal au Cours des Années')
plt.xlabel('Année')
plt.ylabel('Rank')

for i in range(len(df)):
    plt.text(df['Year'][i], df['Rank'][i] + 10,  
             str(df['Rank'][i]),  
             ha='center', fontsize=9, color='black')

plt.show()

