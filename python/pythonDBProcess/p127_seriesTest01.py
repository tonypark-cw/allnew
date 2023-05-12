import pandas as pd

mylist = [10,40,30,20]

myseries = pd.Series(data=mylist, index=['김유신', '이순신', '강감찬', '문무왕'])

print('\nData Type')
print(type(myseries))

myseries.index.name = '점수'
print('\nindex name of series')
print(myseries.index.name)

print('\nname of index')
print(myseries.index)

print('\nprint information of series')
print(myseries)

print('\nrepeat print')
for i in myseries.index:
    print('Index : ' + i + ', Values : '+str(myseries[i]))