import pandas as pd
import matplotlib.pyplot as plt

plt.ion()

data = pd.read_csv('sales.csv')

# access day
days = pd.to_datetime(data['Date']).dt.day
months = pd.to_datetime(data['Date']).dt.month
hours = pd.to_datetime(data['Time']).dt.hour

# save day into a new column in our data frames
data['Day'] = days
data['Month'] = months
data['Hour'] = hours
print(data)

# sales per day
sales_per_day = data.groupby('Day').sum()['Total']
sales_per_month = data.groupby('Month').sum()['Total']
sales_per_hour = data.groupby('Hour').sum()['Total']

# sales_per_day.plot(grid=True)
# sales_per_hour.plot(grid=True)

sales_per_month.plot(kind='bar', grid=True)
