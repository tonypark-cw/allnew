import pandas as pd

d1 = {
    'name':['김유신', '김유신','이순신','박영효','이순신','이순신','김유신'],
    'korean':[60,50,40,80,30,55,45]
}

d2 = {
    'name':['이순신','김유신','신사임당'],
    'english':[60,55,80]
}

df1 = pd.DataFrame(d1)

df2 = pd.DataFrame(d2)

merged_1 = pd.merge(df1, df2, on="name")
print(merged_1)
merged_2 = pd.merge(df1, df2, on="name", how='outer')
print(merged_2)