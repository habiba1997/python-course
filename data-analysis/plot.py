import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('sales.csv')

# Finding Market Share to which location
location_names = [x for x, y in data.groupby('Location')]
total_amount_of_each_location = data.groupby('Location').sum()['Total']

# plot data on bar graph
plt.bar(location_names, total_amount_of_each_location)
plt.show()

plt.pie(total_amount_of_each_location, labels=location_names, autopct='%1.1f%%')
plt.show()


