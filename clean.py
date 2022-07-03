import pandas as pd

df = pd.read_csv('merged.csv')

df.drop(['Unnamed: 0', 'Luminosity'], axis = 1, inplace = True)

final_data = df.dropna()

print(final_data.describe())

final_data.to_csv('final.csv')