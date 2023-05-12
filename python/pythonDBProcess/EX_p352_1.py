import pandas as pd

afile = 'data03.csv'
bfile = 'data04.csv'

atable = pd.read_csv(afile, header=0, encoding='utf-8')
btable = pd.read_csv(bfile, header=0, encoding='utf-8')

print(atable)
print('-' * 50)
print(btable)

atable['반'] ='일반'
btable['반'] ='이반'

mylist = []
mylist.append(atable)
mylist.append(btable)

result = pd.concat(objs=mylist, axis=0, ignore_index=True)
filename = 'result_class.csv'
print(result)
result = result.drop(index=7)
print(result)
result.to_csv(filename, encoding='utf-8')

print(filename, 'saved')