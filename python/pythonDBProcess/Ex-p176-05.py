from pandas import Series, DataFrame
import numpy as np

myindex = ['윤봉길', '김유신', '신사임당']
mylist = [30, 40, 50]

myseries = Series(data=mylist, index=myindex)
print('\n시리즈 출력 결과')
print(myseries)
print()

myindex = ['윤봉길', '김유신', '이순신']
mycolumns = ['용산구', '마포구', '서대문구']
mylist = list(3 * onedata for onedata in range(1, 10)) #여기 모르겠는데... 어케하는거누
# print(mylist)

myframe = DataFrame(np.reshape(np.array(mylist), (3,3)), index=myindex, columns=mycolumns)
print('데이터프레임 출력 결과')
print(myframe)
print()
print('\nDataFrame + Series')
result = myframe.add(myseries, axis=0)
print(result)

myindex2 =['윤봉길', '김유신', '이완용']
mycolumns2 = ['용산구', '마포구', '은평구']
mylist2 = list(5 * onedata for onedata in range(1, 10))

myframe2 = DataFrame(np.reshape(np.array(mylist2), (3, 3)), index=myindex2, columns=mycolumns2)
print('\n데이터프레임 출력 결과')
print(myframe2)

print('\nDataFrame + DataFrame')
result = myframe.add(myframe2, fill_value = 20)
print(result)

print('\nDataFrame - DataFrame')
result = myframe.sub(myframe2, fill_value = 10)
print(result)

# print('\n# 곱하기(mul), 나누기(div)')