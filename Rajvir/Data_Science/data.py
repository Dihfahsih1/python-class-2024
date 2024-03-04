import pandas as pd 

data = {'Name':['raj','charm','mary'],'Age':[19,20,20]}

#reading a csv file
df= pd.read_csv("csv_file2.csv")
# print(df.head())
# print(df.tail())
# (df.['NAME'])
# print(df.loc[100])

#filtering rows based on condition

#adding a column
# df['license']=['AMTI','GTB','LKT']
# print(df)

#Descriptive statistics 
print(df.describe())

#sorting dataframe by a column.
print(df.sort_values(by='Year', ascending=True))