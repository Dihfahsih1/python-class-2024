import pandas as pd

data = {'name':['John','Anna','Peter'],'age':[12,45,67]}

df = pd.DataFrame(data)
#print(df.get('name'))

   #reading a csv file into a dataframe

df = pd.read_csv('csv_file.csv')
  # head for top values
#print(df.head())

  # bottom for low values
#print(df.tail())

   # acessing a single column
#print(df['Year'])

    # accessing details of a row

#print(df.loc[0])

    # accessing data from a specific location or filtering rows based on  a condition

#print(df[df['year'] > 2020])


     # \Descriptive statistics of the dataframe
#print(df.describe())

     #sorting dataframe by a column
    #when ascending is False it will do the oppposite of ascending
print(df.sort_values(by="Year",ascending=True))

     #Dropping  rows or columns  with missing values
#df.dropna(inplace=True)
#print(df)

    #filling missing values with a specific value or values
df.fillna(0,inplace=True)
#print(df)

    #put information in new csv file
df.to_csv('clean_csv.csv',index=False)