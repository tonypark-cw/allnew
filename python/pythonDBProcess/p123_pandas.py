import pandas as pd
import numpy as np

mylist = [10, 40, 30]
myindex = ['김유신', '이순신', '강감찬']

print('\n#Cast 01')
myseries = pd.Series(mylist)
print(myseries)

print('\n#Cast 02')
myseries = pd.Series(data=mylist)
print(myseries)

print('\n#Cast 03')
myseries = pd.Series(data=mylist, index=myindex)
print(myseries)

print('\n#Cast 04')
myseries = pd.Series(data=mylist, index=myindex, dtype=float)
print(myseries)