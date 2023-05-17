import numpy as np
from pandas import DataFrame

myindex = ['이순신', '김유신', '강감찬', '광해군', '연산군']
mycolumns = ['서울', '부산', '광주', '목포', '경주']
mylist = list(10 * onedata for onedata in range(1, 26))
print(mylist)

myframe = DataFrame(np.reshape(mylist, (5, 5)), index=myindex, columns=mycolumns)
print(myframe)

print('\n1 row data read of series')
result = myframe.iloc[1]
print(type(result))
print(result)

print('\nmulti row data read of DataFrame')
result = myframe.iloc[[1, 3]]
print(type(result))
print(result)

print('\neven row data read of DataFrame')
result = myframe.iloc[0::2]
print(type(result))
print(result)

print('\nodd row data read of DataFrame')
result = myframe.iloc[1::2]
print(type(result))
print(result)

print('-'*50)
print('\n김유신 included row data read of DataFrame')
result = myframe.loc[['김유신']]
print(type(result))
print(result)

print('-'*50)
print('\n김유신 included row data read of series')
result = myframe.loc['김유신']
print(type(result))
print(result)

print('-'*50)
print('\n김유신 included row data read of series')
result = myframe.iloc[1]
print(type(result))
print(result)

print('-'*50)
print('\n김유신, 강감찬  / 광주, 목포 included row data read of DF')
result = myframe.loc[['김유신', '강감찬'], ['광주', '목포']]
print(type(result))
print(result)

print('-'*50)
print('\n김유신, 강감찬  / 광주, 목포 included row data read of DF')
result = myframe.iloc[[1, 2], [2, 3]]
print(type(result))
print(result)

print('-'*50)
print('이순신 ~ 강감찬 / 서울 ~ 목포 included row data read of DF')
result = myframe.loc['이순신':'강감찬', '서울':'목포']
print(type(result))
print(result)

print('-'*50)
print('김유신 ~ 광해군 / 부산 included row data read of DF')
result = myframe.loc['김유신':'광해군', ['부산']]
print(type(result))
print(result)


print('-'*50)
print('Boolean Data Process')
result = myframe.loc[[False, True, True, False, True]]
print(result)

print('-'*50)
print('부산 실적 <= 100')
result = myframe.loc[myframe['부산'] <= 100]
print(result)

print('-'*50)
print('목포 실적 == 140')
result = myframe.loc[myframe['목포'] == 140]
print(result)

cond1 = myframe['부산'] >= 70
cond2 = myframe['목포'] >= 140
print('='*50)
print('부산 실적 >= 140 and 목포 실적 >= 140')
print('-'*50)
result = myframe.loc[cond1 & cond2]
print(result)
print('='*50)

print('='*50)
print('부산 실적 >= 140 and 목포 실적 >= 140')
print('-'*50)
df = DataFrame([cond1, cond2])
result = myframe.loc[df.all()]
print(result)
print('='*50)

print('='*50)
print('lambda function')
print('-'*50)
result = myframe.loc[lambda df: df['광주'] >= 80 ]
print(result)
print('='*50)

print('='*50)
print('data set 30 => 이순신, 강감찬 부산 실적')
print('-'*50)
myframe.loc[['이순신', '강감찬'], ['부산']]=30
print(myframe)
print('='*50)

print('='*50)
print('data set 80 => 김유신 ~ 광해군 경주 실적')
print('-'*50)
myframe.loc['김유신':'광해군', ['경주']]=80
print(myframe)
print('='*50)

print('='*50)
print('data set 50 => 연산군 모든 실적')
print('-'*50)
myframe.loc['연산군', :] = 50
print(myframe)
print('='*50)

print('='*50)
print('data set 60 => 모든 사람의 광주 실적')
print('-'*50)
myframe.loc[:, ['광주']] = 60
print(myframe)
print('='*50)

print('='*50)
print('data set 0 => 경주 실적이 60이하인 모든 사람의 경주, 광주 실적')
print('-'*50)
myframe.loc[myframe['경주'] <= 60, ['경주','광주']] = 0
print(myframe)
print('='*50)