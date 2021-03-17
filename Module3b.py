# Matplotlib: how to build various types of plots & customize them to be more visually appealing & interpretable

import pandas as pd
df= pd.read_csv('Gapminder.csv')
print(df)

import matplotlib.pyplot as plt

# Plot this year (hor. axis) and pop (ver. axis) data as a line chart
plt.plot(year, pop)

# How to display the plot? plt.show()
# But before that actually titles & label customizations are needed


# Print the last item from year and pop
print(year[-1])
print(pop[-1])