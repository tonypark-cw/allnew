import pandas as pd

temp = {
    'name':[1,2,34,5,]
}


# afile = 'android.csv'
afile = 'pelicana.csv'
# bfile = 'iphone.csv'
bfile = 'cheogajip.csv'

atable = pd.read_csv(afile, header=0, index_col=0, encoding='utf-8')
btable = pd.read_csv(bfile, header=0, index_col=0, encoding='utf-8')

print(atable)
print('-' * 50)
print(btable)

# atable['android'] ='안드로이드'
atable['pelicana'] ='페리카나'
# btable['iphone'] ='아이폰'
btable['cheogajip'] ='처가집'

mylist = []
mylist.append(atable)
mylist.append(btable)

result = pd.concat(objs=mylist, axis=0, ignore_index=True)
filename = 'chicken_result.csv'
print(result)
result.to_csv(filename, encoding='utf-8')

print(filename, 'saved')