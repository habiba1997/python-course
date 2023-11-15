import pandas as pd
import matplotlib.pyplot as plt

plt.ion()

data = pd.read_csv('sales.csv')

members = data.groupby(['Member', 'Location']).count()['Invoice ID']
members_untacked = members.unstack(level=0)
members_untacked.plot(kind = 'bar')
