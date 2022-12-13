import pandas as pd

df = pd.read_csv('data.csv')

df['Date'] = pd.to_datetime(df['Date'])

df.dropna(subset=['Date'], inplace=True)

df.loc[7, 'Duration'] = 45

for x in df.index:
    if df.loc[x, "Duration"] > 120:
        df.drop(x, inplace=True)

print(df.to_string())

# dropna()
# dropna(inplace =True)
# fillna()
# mean()
# median()
#  mode()
# datetme()
