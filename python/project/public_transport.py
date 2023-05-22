import time

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

from collections import deque

dq = deque()
wait = 3

driver = webdriver.Chrome()
print(type(driver))
print('-'*50)

print('사이트 이동')
url = 'https://www.airkorea.or.kr/web/sidoQualityCompare?itemCode=10008&pMENU_NO=102'
driver.get(url)
time.sleep(wait)

periods = driver.find_elements(By.NAME, 'period')
periods[1].click()
time.sleep(wait)

district = driver.find_element(By.ID, 'district')
district.send_keys('서울')
time.sleep(wait)

month = driver.find_element(By.ID, 'month')
months = month.text.split("\n")
time.sleep(wait)

searches = driver.find_elements(By.CLASS_NAME, 'search')
searches[0].click()
time.sleep(wait)

sido_head = driver.find_element(By.ID, 'sidoTable_thead')
sido = driver.find_element(By.ID, 'sidoTable')
sido_vals = sido.text.split('\n')
header = ['날짜'] + sido_head.text.split(' ')
# print(header)
for m in months:
    month.send_keys(m)
    time.sleep(wait)

    searches = driver.find_elements(By.CLASS_NAME, 'search')
    searches[0].click()
    time.sleep(wait)

    for sido_val in sido_vals:
        dq.append(sido_val.split(' '))

    time.sleep(wait)
    print(dq)
    # break

df = pd.DataFrame(dq, columns=header)
print(df)
df.to_csv('/home/ubuntu/시도별대기정보PM25.csv', encoding='utf-8')

driver.quit()