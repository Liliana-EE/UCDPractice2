#Introduction to Importing Data
# Importing entire text files

# Open a file: file
filename = 'moby_dick.txt'
file = open(filename, mode= 'r')
text = file.read()

# Print it
print(file.read())

# Check whether file is closed
print(file.closed)

# Close file
file.close()

# Check whether file is closed
print(file.closed)

#Importing text files line by line

# Read & print the first 3 lines
with open('moby_dick.txt') as file:
    print(file.readline())
    print(file.readline())
    print(file.readline())

#Importing different datatypes
import matplotlib.pyplot as plt

# Import numpy
import numpy as np

# Assign filename: file
file = 'seaslug.txt'

# Import file: data
data = np.loadtxt(file, delimiter='\t', dtype=str)

# Print the first element of data
print(data[0])

# Import data as floats and skip the first row: data_float
data_float = np.loadtxt(file, delimiter='\t', dtype=float, skiprows=1)

# Print the 10th element of data_float
print(data_float[9])

# Plot a scatterplot of the data
plt.scatter(data_float[:, 0], data_float[:, 1])
plt.xlabel('time (min.)')
plt.ylabel('percentage of larvae')
plt.show()

#Working with mixed datatypes
# Assign the filename: file
file = 'Titanic.csv'

# Import file using np.recfromcsv: d
d = np.recfromcsv('Titanic.csv', delimiter=',', names=True, dtype=None)

# Print out first three entries of d
print(d[:3])

#Importing flat files using pandas
# Import pandas as pd
import pandas as pd

# Assign the filename: file
file = 'Titanic.csv'

# Read the file into a DataFrame: df
df = pd.read_csv(file)

# View the head of the DataFrame
print(df.head())
