import pandas as pd
import matplotlib.pyplot as plt

plt.ion()

data = pd.read_csv('sales.csv')

product_line = data.groupby(['Gender', 'Category']).count()['City']
unstacked = product_line.unstack(level=0)
unstacked.plot(kind='bar')
