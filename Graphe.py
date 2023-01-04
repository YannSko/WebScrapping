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
