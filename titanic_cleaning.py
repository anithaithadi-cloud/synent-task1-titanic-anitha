import pandas as pd

df = pd.read_csv('titanic.csv')
print(df.head())

df['Age'].fillna(df['Age'].median(), inplace=True)
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)
df.drop_duplicates(inplace=True)

df.to_csv('cleaned_titanic.csv', index=False)

print("Data Cleaning Done")
