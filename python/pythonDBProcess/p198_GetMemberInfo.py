import pandas as pd

filename = 'memberInfo.csv'
df = pd.read_csv(filename)
print(df)
print(type(df))
member = pd.DataFrame(df)
print(member)
print(type(member))

newdf01 = df.set_index(keys=['id'])
print(newdf01)

newdf02 = df.set_index(keys=['id'], drop=False)
print(newdf02)

df2 = pd.read_csv(filename, index_col='id')
print(df2)