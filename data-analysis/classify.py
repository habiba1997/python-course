import pandas as pd
import matplotlib.pyplot as plt
plt.ion()

data = pd.read_csv('sales.csv')
# you can change Invoice ID to any column because all will have the smae count number
location_sales = data.groupby(['Gender', 'Location']).count()['Invoice ID']
print(location_sales)

# we need to unstack this into row and column to simple data frame ( column row format) to be plotted
# level 0 because its  3-dimensional frame that need to be 2 dimensions
unstacked_data = location_sales.unstack(level=0)
print(unstacked_data)

unstacked_data.plot(kind='bar')
