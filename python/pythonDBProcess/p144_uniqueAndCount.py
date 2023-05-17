from pandas import Series

print('\nUniuqe, count, isin')
mylist = ['라일락', '코스모스', '코스모스', '백일홍', '코스모스', '코스모스', '들장미', '들장미', '라일락', '제비꽃', '라일락']
myseries = Series(mylist)

print('\nUnique()')
print(myseries.unique())
print('-'*50)

print('\nCount()')
print(myseries.count())
print('-'*50)

print('\nisIn()')
print(myseries.isin(['코스모스','라일락']))
print('-'*50)

print('\nmask')
print(myseries[myseries.isin(['코스모스','라일락'])])
print('-'*50)
