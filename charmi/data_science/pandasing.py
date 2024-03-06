import pandas as pd     

data = {'Name': ['Charmi', 'Rajvir', 'John'], 'Age': [20,23,45]}

df = pd.DataFrame(data)      #df is dataframe

# print(df)
# print(df.get('Name'))

#reading csv file

df = pd.read_csv("csv_file2.csv")
# print(df)

#print(df['Year'])            #for accessing a specific coloumn

# print(df.tail())          #for accessing the end of the file

# print(df.loc[0])

# print(df[df['Year']> 2020])        #for filtering rows based on a condition

#print(df.describe())        #for describing the file

print(df.sort_values(by= "Year",ascending=True))     #for sorting value. the 'by' argument is a must for sort_values
