import time

import pandas as pd
from bs4 import BeautifulSoup
from collections import deque

f = open("weather_data.txt", 'r', encoding='utf-8')
weather = ""
i = 1
f.readline()

dq = deque()

yy = 2019
mm = 0

dd = 1
while True:
    temp = f.readline()
    row1 = temp.split('\t')
    temp = f.readline()
    row2 = temp.split('\t')
    # print(row1, row2)
    for i in range(len(row1)):
        value = {}
        if len(row1[i]) > 0:
            # print(row1[i].split('일')[0])
            try:
                dd = int(row1[i].split('일')[0])
                if dd == 1:
                    if mm <= 11:
                        mm += 1
                    else:
                        mm = 1
                        yy += 1
            except:
                if row1[i].split('일')[0] == '\n':
                    continue

            value['날짜'] = str(yy) + '-' + str(mm).zfill(2) + '-' + str(dd).zfill(2)
            row2[i] = row2[i].replace(' -', '0')
            for r in row2[i].split(' '):
                if len(r) > 1:
                    # print(r.split(':'))
                    val = r.split(':')[1]
                    val = val.replace('\n','')
                    value[r.split(':')[0]] = val
        if len(value) > 0:
            dq.append(value)
            # print(value)
    if not temp:
        break
    weather += temp
f.close()
# for d in dq:
#     print(d)
df = pd.DataFrame(dq, columns=list(dq[0].keys()))
# print(df)
df = df.dropna()
# print(df)

df.to_csv('WEATHER.csv', encoding='utf-8', index=False)

df1 = pd.read_csv('WEATHER.csv', encoding='utf-8')
df1['평균기온'] = df1['평균기온'].str[:-1]
df1['최고기온'] = df1['최고기온'].str[:-1]
df1['최저기온'] = df1['최저기온'].str[:-1]
df1['일강수량'] = df1['일강수량'].str.replace('mm','')
# print(df1)

df1 = df1.astype({'평균기온': 'float', '최고기온': 'float','최저기온': 'float','평균운량': 'float','일강수량': 'float'})
# print(df1.info())
df2 = pd.read_csv('KOSPI.csv', encoding='utf-8')
df2 = df2.dropna()
df2['종가'] = df2['종가'].str.replace(',', '')
df2['시가'] = df2['시가'].str.replace(',', '')
df2['고가'] = df2['고가'].str.replace(',', '')
df2['저가'] = df2['저가'].str.replace(',', '')

for i in df2[df2['거래량'].str.contains('K',na=False)].index:
    df2.at[i,'거래량'] = float(df2.at[i,'거래량'][:-1])* 1000
for i in df2[df2['거래량'].str.contains('M',na=False)].index:
    df2.at[i,'거래량'] = float(df2.at[i,'거래량'][:-1])* 1000000
for i in df2[df2['거래량'].str.contains('B',na=False)].index:
    df2.at[i,'거래량'] = float(df2.at[i,'거래량'][:-1])* 1000000000

# print(df2)
df2['변동 %'] = df2['변동 %'].str.replace('%', '')
df2 = df2.astype({'종가': 'float', '시가': 'float','고가': 'float','저가': 'float','거래량': 'float','변동 %': 'float'})
print(df2)

df3 = pd.merge(df1[['날짜','평균기온', '최고기온', '최저기온','평균운량','일강수량']], df2[['날짜','종가','시가','고가','저가','거래량','변동 %']], left_on='날짜',right_on='날짜', how='inner')
data = df3.drop(['날짜'], axis=1)
# print(data.corr())
# print(df3.corr())

data.columns = ['MEAN_TEMP', 'MAX_TEMP',"MIN_TEMP", "DAY_CLD","DAY_RAIN", "END_PRI", "BGN_PRI","MAX_PRI","MIN_PRI","AMOUNT", "VAR"]

# print(data)

import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(15,15))
sns.heatmap(data=data.corr(), annot=True, fmt = '.2f', linewidths=.5, cmap='Reds')
plt.show()