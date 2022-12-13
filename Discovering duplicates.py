import pandas as pd

df = pd.read_csv('data.csv')

df.drop_duplicates(inplace=True)


print(df.to_string())


# duplicated()
# drop_duplicates()