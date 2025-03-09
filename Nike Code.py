import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

file_path ='Nike_Stats.xlsx'

#1er graph
df = pd.read_excel(file_path, sheet_name='Feuil1')


plt.figure(figsize=(10, 6))
plt.bar(df['Année'], df['Revenu (millions de $)'], color='#10befb')          
plt.title('Revenus de Nike par Année (Millions $)')
plt.xlabel('Année')
plt.ylabel('Revenu (millions de $)')

for i in range(len(df)):
    if i % 2 == 0:  
        plt.text(df['Année'][i], df['Revenu (millions de $)'][i] + 10,  
                 str(df['Revenu (millions de $)'][i]),  
                 ha='center', fontsize=9, color='black')

#2ème grapg
df =pd.read_excel(file_path, sheet_name='Feuil1')

plt.figure(figsize=(10, 6))
plt.bar(df['Année'], df['Nombre de magasins'], color='#feaa01')
plt.title('Nombre de Magasins Nike par Année')
plt.xlabel('Année')
plt.ylabel('Nombre de Magasins')

for i in range(len(df)):
    plt.text(df['Année'][i], df['Nombre de magasins'][i] + 10,  
             str(df['Nombre de magasins'][i]),  
             ha='center', fontsize=9, color='black')


#2ème graph
df = pd.read_excel(file_path, sheet_name='Segment')

labels = df['Segment']
values = df['Valeur']

plt.title('CA de la Marque Nike par Segment')
plt.figure(figsize=(10, 6))
plt.pie(values, labels= labels, autopct='%1.1f%%', startangle=140,
        colors=['#f63b58', '#10befb', '#feaa01', '#0ae881'], 
        wedgeprops={'edgecolor': 'black'})

#3ème graph
df= pd.read_excel(file_path, sheet_name='Pub')

plt.figure(figsize=(10, 6))
plt.plot(df['Année'], df['Coûts de publicité et de promotion de Nike'], marker ='o', color='#f63b58', linestyle='-')
plt.title('Coûts de Publicité et de Promotion de Nike (monde)')
plt.xlabel('Année')
plt.ylabel('Coûts Pub & Promotion')
plt.grid(True)
plt.tight_layout()

plt.show()