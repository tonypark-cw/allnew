import time
from selenium import webdriver
from selenium.webdriver.common.by import By
# filepath = 'C:/Users/박찬우/Downloads/chromedriver_win32/chromedriver.exe'

driver = webdriver.Chrome()
print(type(driver))


print('-'*50)

print('Go google')

# url = 'https://www.google.com'
url = 'https://www.naver.com'
driver.get(url)

search_textbox = driver.find_element(By.NAME, 'query')
# word = '한미 핵 회담'
word = '아이유'
search_textbox.send_keys(word)
search_textbox.submit()

wait = 3
print(str(wait) + '초 동안 기다리세요')
time.sleep(wait)

imagefile = 'iu.png'
driver.save_screenshot(imagefile)
print(imagefile + '이미지 저장')
driver.implicitly_wait(wait)

driver.quit()
