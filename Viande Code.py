import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file_path = 'Conso_Viande_France_Stats.xlsx'

#1er graph
df = pd.read_excel(file_path, sheet_name='Feuil1')

plt.figure(figsize=(10, 6))
plt.plot(df['Année'], df['Conso Total Brute de Viande en France'],marker ='o', linestyle='-', color='#f60487')
plt.title('Consommation Totale Brute de Viande en France (en tonnes équivalent-carcasse)')
plt.xlabel('Année')
plt.ylabel('Conso Brut de Viande (en tonnes équivalent-carcasse)')

for i in range(len(df)):
    plt.text(df['Année'][i], df['Conso Total Brute de Viande en France'][i] + 10,  
             str(df['Conso Total Brute de Viande en France'][i]),  
             ha='center', fontsize=9, color='black')

#2ème graph
plt.figure(figsize=(10, 6))
plt.plot(df['Année'], df['Consommation de Viande par Habitant en France'], marker='o', linestyle='-', color='#5be0f6')
plt.title('Consommation de Viande par Habitant en France (kg équivalent-carcasse)')
plt.xlabel('Année')
plt.ylabel('Conso Viande / par Habitant')

for i in range(len(df)):
    plt.text(df['Année'][i], df['Consommation de Viande par Habitant en France'][i] + 10,  
             str(df['Consommation de Viande par Habitant en France'][i]),  
             ha='center', fontsize=9, color='black')
    


plt.show()