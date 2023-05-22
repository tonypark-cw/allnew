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
BASE_URL = 'https://www.airkorea.or.kr/web/sidoQualityCompare'
URL_LISTS = ['?itemCode=10008&pMENU_NO=102',
             '?itemCode=10007&pMENU_NO=101',
             '?itemCode=10003&pMENU_NO=103',
             '?itemCode=10006&pMENU_NO=104',
             '?itemCode=10002&pMENU_NO=105',
             '?itemCode=10001&pMENU_NO=106']

print('사이트 이동')
url = 'https://www.airkorea.or.kr/web/sidoQualityCompare?itemCode=10008&pMENU_NO=102'

for url_end in URL_LISTS:

    url = BASE_URL + url_end
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
    df.to_csv(url_end[1:15] + '.csv', encoding='utf-8')

driver.quit()