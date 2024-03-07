import pandas as pd

data = {'Name':['John','Anna','Peter'], 'Age':[12,45,67]}

df=pd.DataFrame(data)

print(df.get('Age'))

#reading a csv file into a dataframe
df=pd.read_csv('csv_file.csv')
print(df.loc[40000])
print(df[df['Year'] > 2020])
print(df.describe())

print(df.sort_values(by="Year",ascending=False))

#Dropping rows or columns with missing values
df.dropna(inplace=True)
print(df)

#filling missing values with a sepecific values
df.fillna(0,inplace=True)
print(df)

df.to_csv('cleaned_data.csv',index=False)
