import pandas as pd

mystorefile = 'store.csv'
mystore = pd.read_csv(mystorefile, encoding='utf-8', index_col=0, header=0)

print('\n매장 테이블')
print(mystore)

districtfile = 'districtmini.csv'
mydistrict = pd.read_csv(districtfile, encoding='utf-8', index_col=0, header=0)
print('\n행정 구역 테이블')
print(mydistrict)

result = pd.merge(mystore, mydistrict, on=['sido', 'gungu'], how='outer', suffixes=['', '_'], indicator=True)
print('\nMerge Result')
print(result)

m_result = result.query('_merge == "left_only"')
print('\n왼쪽에만 있는 방')
print(m_result)

gungufile = open('./gungufile.txt', encoding='utf-8')
gungu_list = gungufile.readlines()

gungu_dict = {}
for onegu in gungu_list:
    mydata = onegu.replace('\n', '').split(':')
    gungu_dict[mydata[0]] = mydata[1]
print('\n군구 사전 내용')
print(gungu_dict)

mystore.gungu = mystore.gungu.apply(lambda data : gungu_dict.get(data, data))

print('\n수정된 가게 정보 출력')
print(gungu_dict)
