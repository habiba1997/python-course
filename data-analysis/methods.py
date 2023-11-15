import pandas as pd

data = pd.read_csv('sales.csv')

print(data)
# print row number 200 but with data column names
# access each individual row
print(data.iloc[200])

# print distinct values of column category
# access each individual column
print(data['Category'].unique())

# select data depend on certain condition
# 1st 10 records
print(data[data['Gender'] == 'Male'].head(10))
# can add as many queries as you want
print(data.query('City=="NewYork" & Payment=="Cash"'))

# sum total of numeric value
print(data.sum()['Total'])

# Max of each column
print(data.max())  # max(), sum(), min(), mean() all exist

print(data[data['Total'] == data.max()['Total']])

# Group By
# I want to combine all data total for each city
# sum up all the sales on each city (can also be done on each date or any other column)
print(data.groupby('City').sum()['Total'])

