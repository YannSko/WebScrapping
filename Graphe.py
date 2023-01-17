import matplotlib.pyplot as plt

import pandas as pd

import csv

from collections import Counter

​

with open('ECommerce_consumer behaviour.csv', newline='') as csvfile:

    reader = csv.DictReader(csvfile)

    for row in reader:

        

        #print(row['department'])

        list=[]

        list.append(row['department'])

        #print(list[i])

        

​

counts = Counter(list)

print(counts)        

#df = pd.read_csv('ECommerce_consumer behaviour.csv')

#data = df['department']

#plt.pie(data, labels=data.unique(), colors=['red', 'green', 'blue'])

​

#plt.show()

​

Counter({'product'})

import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns
print("Setup Complete")


Coffee_Filepath = "coffee_analysis.csv"
Coffee_Data = pd.read_csv(Coffee_Filepath, index_col="name")
Coffee_Data

# Largeur et hauteur du graph
plt.figure(figsize=(10,6))


plt.title("Lien entre prix et type du café")

# Bar chart 
sns.barplot(x=Coffee_Data['roast'], y=Coffee_Data['100g_USD'])

# lab de chaque ax
plt.ylabel("Prix moyen au 100g")
plt.xlabel(" Type de café")


