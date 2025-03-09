import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

file_path = 'Cigarette_Stats.xlsx'

#1er graph
df = pd.read_excel(file_path, sheet_name='Cigarette')

plt.figure(figsize=(10, 6))
plt.bar(df['Année'], df['Cigarettes Vendues (en Milliards)'], color='#5fe0f6')          
plt.title('Nombre de Cigarettes Vendues (en Milliards) en France')
plt.xlabel('Année')
plt.ylabel('Nombre de Cigarettes Vendues')

for i in range(len(df)):
    plt.text(df['Année'][i], df['Cigarettes Vendues (en Milliards)'][i] + 1 ,  
             str(df['Cigarettes Vendues (en Milliards)'][i]),  
             ha='center', fontsize=9, color='black')
    

#2ème graph
df = pd.read_excel(file_path, sheet_name='Cigarette')

plt.figure(figsize=(10, 6))
plt.plot(df['Année'], df['Prix paquet de cigarettes'],marker='o', linestyle='-', color='#ea108d')
plt.title('Évolution du Prix du Paquet de Cigarettes en France')
plt.xlabel('Année')
plt.ylabel('Prix du Paquet de Cigarettes')

for i in range(len(df)):
    plt.text(df['Année'][i], df['Prix paquet de cigarettes'][i],  
             str(df['Prix paquet de cigarettes'][i]),  
             ha='center', fontsize=9, color='black')
    
plt.show()