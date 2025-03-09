import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

file_path = 'Hamilton_vs_Verstappen_Stats.xlsx'

#1er graph
df = pd.read_excel(file_path, sheet_name='Feuil1')

plt.figure(figsize=(10, 6 ))
plt.plot(df['Année'], df['Position'], marker='o', linestyle='-', color='#0167f8')
plt.title('Rank de Verstappen en fin de Saison par Année')
plt.xlabel('Année')
plt.ylabel('Rank')

for i in range(len(df)):
    plt.text(df['Année'][i], df['Position'][i] + 0,  
             str(df['Position'][i]),  
             ha='center', fontsize=9, color='black')

#2ème graph
df = pd.read_excel(file_path, sheet_name='Feuil2')

plt.figure(figsize=(10, 6))
plt.plot(df['Année'], df['Position'],marker='o', linestyle='-', color='#ffe047')
plt.title('Rank d\Hamilton en fin de Saison par Année')
plt.xlabel('Année')
plt.ylabel('Rank')

for i in range(len(df)):
    plt.text(df['Année'][i], df['Position'][i] + 0,  
             str(df['Position'][i]),  
             ha='center', fontsize=9, color='black')

plt.show()