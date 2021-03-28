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

# SORTING AND SUBSETTING
#Sorting Rows

# 1. Sort homelessness by the number of homeless individuals, from smallest to largest, and save this as homelessness_ind
# Sort homelessness by individual
homelessness_ind = homelessness.sort_values('individuals', ascending =True)

# Print the top few rows
print(homelessness_ind.head())

# 2. Sort homelessness by the number of homeless family_members in descending order, and save this as homelessness_fam
# Sort homelessness by descending family members
homelessness_fam = homelessness.sort_values('family_members', ascending =False)

# Print the top few rows
print(homelessness_fam.head())

#3. Sort homelessness first by region (ascending), and then by number of family members (descending)
# Sort homelessness by region, then descending family members
homelessness_reg_fam = homelessness.sort_values(['region','family_members'],ascending=[True,False])

# Print the top few rows
print(homelessness_reg_fam.head())

# Subsetting columns

# 1. Create a DataFrame called individuals that contains only the individuals column of homelessness.
# Select the individuals column
individuals = homelessness['individuals']

# Print the head of the result
print(individuals.head())

# 2. Create a DataFrame called state_fam that contains only the state and family_members columns of homelessness, in that order.
# Select the state and family_members columns
state_fam = homelessness[['state','family_members']]

# Print the head of the result
print(state_fam.head())

#3. Create a DataFrame called ind_state that contains the individuals and state columns of homelessness, in that order
# Select only the individuals and state columns, in that order
ind_state = homelessness[['individuals','state']]

# Print the head of the result
print(ind_state.head())

# SUBSETTING ROWS
# 1. Filter homelessness for cases where the number of individuals is greater than ten thousand, assigning to ind_gt_10k. View the printed result.
# Filter for rows where individuals is greater than 10000
ind_gt_10k = homelessness[homelessness['individuals']>10000]

# See the result
print(ind_gt_10k)

# 2. Filter homelessness for cases where the USA Census region is "Mountain", assigning to mountain_reg. View the printed result.
# Filter for rows where region is Mountain
mountain_reg = homelessness[homelessness['region']=='Mountain']

# See the result
print(mountain_reg)

#3. Filter homelessness for cases where the number of family_members is less than one thousand and the region is "Pacific", assigning to fam_lt_1k_pac. View the printed result.
# Filter for rows where family_members is less than 1000
# and region is Pacific
fam_lt_1k_pac = homelessness[(homelessness['family_members']<1000)&(homelessness['region']=='Pacific')]

# See the result
print(fam_lt_1k_pac)

# Using square brackets plus logical conditions is often the most powerful way of identifying interesting rows of data.
# Subsetting rows by categorical variables

#1. Filter homelessness for cases where the USA census region is "South Atlantic" or it is "Mid-Atlantic", assigning to south_mid_atlantic. View the printed result.
# Subset for rows in South Atlantic or Mid-Atlantic regions
south_mid_atlantic = homelessness[(homelessness["region"]=="South Atlantic") | (homelessness["region"]=="Mid-Atlantic")]

# See the result
print(south_mid_atlantic)

#2. Filter homelessness for cases where the USA census state is in the list of Mojave states, canu, assigning to mojave_homelessness. View the printed result.
# The Mojave Desert states
canu = ["California", "Arizona", "Nevada", "Utah"]

# Filter for rows in the Mojave Desert states
mojave_homelessness = homelessness[homelessness['state'].isin(canu)]

# See the result
print(mojave_homelessness)

# Adding New Columns

# Add a new column to homelessness, named total, containing the sum of the individuals and family_members columns.
# Add another column to homelessness, named p_individuals, containing the proportion of homeless people in each state who are individuals.

# Add total col as sum of individuals and family_members
homelessness['total'] = homelessness['individuals'] + homelessness['family_members']

# Add p_individuals col as proportion of individuals
homelessness['p_individuals'] = homelessness['individuals'] / homelessness['total']


# See the result
print(homelessness)

#COMBO ATTACK
# Add a column to homelessness, indiv_per_10k, containing the number of homeless individuals per ten thousand people in each state.
# Subset rows where indiv_per_10k is higher than 20, assigning to high_homelessness.
# Sort high_homelessness by descending indiv_per_10k, assigning to high_homelessness_srt.
# Select only the state and indiv_per_10k columns of high_homelessness_srt and save as result. Look at the result.

# Create indiv_per_10k col as homeless individuals per 10k state pop
homelessness["indiv_per_10k"] = 10000 * homelessness['individuals'] / homelessness['state_pop']

# Subset rows for indiv_per_10k greater than 20
high_homelessness = homelessness[homelessness['indiv_per_10k']>20]

# Sort high_homelessness by descending indiv_per_10k
high_homelessness_srt = high_homelessness.sort_values('indiv_per_10k',ascending=False)

# From high_homelessness_srt, select the state and indiv_per_10k cols
result = high_homelessness_srt[['state', 'indiv_per_10k']]

# See the result
print(result)

# Washington, D.C. has the highest number of homeless individuals - almost 54 per ten thousand people.
# This is almost double the number of the next-highest state, Hawaii. If you combine new column addition,
# row subsetting, sorting, and column selection, you can answer lots of questions like this.

