import pandas as pd

mylist = [200,300,400,100]
myseries = pd.Series(data=mylist, index=['손오공','저팔계','사오정','삼장법사'])

myseries.name = '직원 실적'
myseries.index.name = '실적 현황'

print(myseries)

print(myseries.name)

print(myseries.index.name)

for k,v in myseries.items():
    print('색인 : ' + k + ', 값 : ' +str(v))

myindex = ['강감찬', '이순신','김유신','광해군','연산군','을지문덕']
mylist = [50,60,40,80,70,20]
myseries=pd.Series(data=mylist, index=myindex)
print(myseries)

myseries[1] = 100
print(myseries)

myseries[2:5] = 999
print(myseries)

myseries[['강감찬', '을지문덕']] = 30
print(myseries)

myindex1 = ['성춘향', '이몽룡','심봉사']
mylist1 = [40,50,60]
myseries1 =pd.Series(data=mylist1, index=myindex1)
print(myseries1)

myindex2 = ['성춘향', '이몽룡','뺑덕어멈']
mylist2 = [20,40,70]
myseries2 =pd.Series(data=mylist2, index=myindex2)
print(myseries2)

print(myseries1.add(myseries2,fill_value=10))

print(myseries1.subtract(myseries2,fill_value=30))

sdata = {
    '국어':[40,60,80,50,30],
    '영어':[55,65,75,85,60],
    '수학':[30,40,50,60,70]
}
idx = ['강감찬', '이순신','김유신','김구','안중근']
df = pd.DataFrame(sdata, index=idx)
print(df)

print(df.iloc[1::2])

print(df.loc[['이순신']])

print(df.loc[['강감찬'],['영어']])

print(df.loc[['안중근', '강감찬'],['국어','수학']])

print(df)

df.loc[['이순신', '강감찬'],['영어']] = 80
print(df)

df.loc['이순신':'김구',['수학']] = 100
print(df)

myindex = ['윤봉길','김유신', '신사임당']
mylist = [30,40,50]
myseries =pd.Series(data=mylist, index=myindex)
print(myseries)

sdata = {
    '용산구':[3,12,21],
    '마포구':[6,15,24],
    '서대문구':[9,18,27]
}
idx = ['윤봉길','김유신', '이순신']
myframe = pd.DataFrame(sdata, index=idx)
print(myframe)

sdata2 = {
    '용산구':[5,20,35],
    '마포구':[10,25, 40],
    '은평구':[15, 30, 45]
}
idx2 = ['윤봉길','김유신', '이완용']
myframe2 = pd.DataFrame(sdata2, index=idx2)
print(myframe2)

print(myframe.add(myseries, axis=0))

print(myframe.add(myframe2, fill_value=20 ))

print(myframe.subtract(myframe2, fill_value= 10 ))

df = pd.read_csv('data02.csv', header=None, names=['이름', '학년', '국어', '영어', '수학'], index_col=['이름'])
print(df)

df.iloc[0,2] = 40
df.iloc[2,1] = 30
print(df)

mycolumns = ('이름', '나이')
myencoding = 'utf-8'
mydata = [('김철수',10), ('박영희',20)]

filename = 'csv_02_01.csv'
myframe = pd.DataFrame(mydata, columns=mycolumns)
print(myframe)
myframe.to_csv(filename, encoding=myencoding, mode='w', index=False)

filename = 'csv_02_02.csv'
myframe = pd.DataFrame(mydata, columns=mycolumns)
print(myframe)
myframe.to_csv(filename, encoding=myencoding, mode='w', index=False, sep="#")