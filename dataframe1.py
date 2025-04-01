import pandas as pd 

data = {
    "Name": ["Alice","Mehdi","Bob"],
    "Age": [20, 24, 21],
    "City": ["London","Givet","Tokyo"]
}


df = pd.DataFrame(data)

#selectionner plusieurs colonnes
#print(df[['Age','Name']])

#print index
#print(df.loc[0])

#print row
#print(df['Name'])

#select row in range
#print(df.iloc[0:2])

#over_18 = df[(df["Age"]) > 30 | (df['City'] == 'Givet')]

#the better way
#print(df.query("Age > 18 and City == 'Givet'"))

age = df.query("Age < 30")
age_berlin = df.query("Age > 30 or City == 'Tokyo'")

df.loc[1, 'City'] = 'Berlin'
df.loc[1, 'Age'] = 10000
#print(df.iloc[1])

df['Country'] = ['UK','France','Japan']
print(df['Country'])
