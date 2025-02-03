import pandas as pd 

df =  pd.read_csv('Employee-Attrition.csv')

first_two = df.head(2).to_json(orient='records', indent=4)
with open('first_two.json', 'w') as f:
    f.write(first_two)

print(first_two)
