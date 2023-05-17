from pandas import Series, DataFrame

myindex1 = ['강호민', '유재준', '김제명', '신동진']
mylist1 = [30, 40, 50, 60]

myindex2 = ['강호민', '유재준', '김제명', '이수진']
mylist2 = [30, 40, 50, 70]

myseries1 = Series(data=mylist1, index=myindex1)
myseries2 = Series(data=mylist2, index=myindex2)

print('\n# data of series1')
print(myseries1)
print('\n# data of series2')
print(myseries2)

print('\n# myseries1 + 5')
print(myseries1 + 5)
print('-'*50)

print('\n# myseries1 - 5')
print(myseries1 - 5)
print('-'*50)

print('\n# myseries1 * 5')
print(myseries1 * 5)
print('-'*50)

print('\n# myseries1 / 5')
print(myseries1 / 5)
print('-'*50)

print('\n# myseries1 >= 35')
print(myseries1 >= 35)
print('-'*50)

print('\nadd of series(if there is nodata then, NaN)')
print(myseries1 + myseries2)
print('-'*50)

print('\nsub of series(operation after fill value 0)')
print(myseries1.sub(myseries2, fill_value=0))
print('-'*50)

