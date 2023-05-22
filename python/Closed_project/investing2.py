import time

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

from collections import deque


# filepath = 'C:/Users/박찬우/Downloads/chromedriver_win32/chromedriver.exe'
wait = 3

f = open("KOSPI.txt", 'r', encoding='utf-8')
html = ""
while True:
    temp = f.readline()
    if not temp:
        break
    html += temp
    # print(html)
f.close()


html_result = BeautifulSoup(html, 'html.parser')


print(type(html_result))
print('-'*50)

# 컬럼 name
thead = html_result.select('thead')
head = []
for tval in thead:
    candi = tval.select('span')
    for c in candi:
        if len(c.text) > 0:
            head.append(c.text)
print('-'*50)


# 컬럼 value
dq = deque()
tbody = html_result.select('tbody')
for trow in tbody:
    td = trow.select('td')
    temp = []
    for val in td:
        if len(val.select('time')) > 0:
            if len(temp) > 0:
                dq.append(temp)
            temp = []
        temp.append(val.text.replace(' ', ''))
        print(val.text)
# print(dq)

df = pd.DataFrame(dq, columns=head)
print(df)
df.to_csv('KOSPI.csv', encoding='utf-8', index=False)

