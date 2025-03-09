import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

file_path = 'Natalité_Stats.xlsx'

#1er graph
df = pd.read_excel(file_path, sheet_name='Feuil3')

plt.figure(figsize=(10, 6 ))
plt.plot(df['Année'], df['Nombre de naissances'], marker='o', linestyle='-', color='#f36472')
plt.title('Nombre de Naissances en France de 1900 à 2019 (en milliers)')
plt.xlabel('Année')
plt.ylabel('Nombre de Naissances')

#2ème graph
df =pd.read_excel(file_path, sheet_name='Feuil1')

plt.figure(figsize=(10, 6 ))
plt.bar(df['Année'], df['Taux de Mortalité'], color='#5a85fc')
plt.title('Taux de Mortalité en France de 2004 à 2023 (pour 1000 habitants)')
plt.xlabel('Année')
plt.ylabel('Taux de Mortalité')

for i in range(len(df)):
    plt.text(df['Année'][i], df['Taux de Mortalité'][i],  
             str(df['Taux de Mortalité'][i]),  
             ha='center', fontsize=9, color='black')

print(df)

plt.show()