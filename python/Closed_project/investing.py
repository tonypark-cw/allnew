import time

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

from collections import deque


# filepath = 'C:/Users/박찬우/Downloads/chromedriver_win32/chromedriver.exe'
wait = 3

driver = webdriver.Chrome()
print(type(driver))
print('-'*50)

print('사이트 이동')
url = 'https://kr.investing.com/indices/kospi-historical-data'
driver.get(url)
time.sleep(wait*10)

#날짜 지정 탭에 19년 1월 1일 부터 오늘 날짜까지 지정 필요.
print('달력 클릭')
date_class = "historical-data_history-date-picker-wrapper__dDOuq"
date_tab = driver.find_element(By.CLASS_NAME, date_class)
date_tab.click()

time.sleep(wait)
print('날짜 입력')
start_date = date_tab.find_element(By.TAG_NAME, 'input')
start_date.send_keys("2019-01-01")

time.sleep(wait)
print('적용 하기')
btn_class = "HistoryDatePicker_HistoryDatePicker__sjrlU"
apply_btn = driver.find_element(By.CLASS_NAME, date_class).find_element(By.TAG_NAME, 'button')
apply_btn.click()


time.sleep(wait)
print('결과 보기')
# result_class = "border border-main"
results = driver.find_elements(By.TAG_NAME, 'table')


datas = ""
for i, result in enumerate(results):
    if result.text.__sizeof__() > 1000:
        print('-'*50)
        print(i)
        datas += result.get_attribute('innerHTML')

        # html_result = BeautifulSoup(datas, 'html.parser')
        # print(html_result)
f = open("KOSPI.txt", 'w', encoding='utf-8')
f.write(str(datas))
f.close()
print(datas)
# print(type(html_result))
print('-'*50)
# head = []
# thead = html_result.select('thead')
# for tval in thead:
#     candi = tval.select('span')
#     for c in candi:
#         if len(c.text) > 0:
#             head.append(c.text)
# print(head)
# print('-'*50)
# tbody = html_result.select('tbody')
# for trow in tbody:
#     td = trow.select('td')
#     for val in td:
#         print(val)

driver.quit()

# deque
# list = []
# list  ['']

