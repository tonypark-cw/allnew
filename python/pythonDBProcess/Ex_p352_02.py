import pandas as pd

dict1 = {
    'name' : ['김유신', '김유신', '이순신', '박영호', '이순신', '이순신', '김유신'],
    'korean' : [60, 50, 40, 80, 30, 55, 45]
}
dict2 = {
    'name' : ['이순신', '김유신', '신사임당'],
    'English' : [60, 55, 80]
}

newdict1 = pd.DataFrame(dict1)
newdict2 = pd.DataFrame(dict2)

merge1 = pd.merge(newdict1, newdict2, on='name')
print(merge1)
merge2 = pd.merge(newdict1, newdict2, on='name', how='outer')
print(merge2)