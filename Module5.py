#Inspecting a DataFrame

import pandas as pd
data=pd.read_csv('homelessness.csv')
homelessness = data

# Print the head of the homelessness data
print(homelessness.head())

# Print information about homelessness
print(homelessness.info())

# Print information about the column types and missing values in homelessness.
print(homelessness.shape)

# Print a description of homelessness
print(homelessness.describe())

#Parts of a DataFrame

# Print the values of homelessness
print(homelessness.values)

# Print the column index of homelessness
print(homelessness.columns)

# Print the row index of homelessness
print(homelessness.index)
