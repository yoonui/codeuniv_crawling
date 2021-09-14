# 동적 크롤링 1 _ 문제

from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options)


url = 'https://papago.naver.com/'
driver.get(url)
time.sleep(2)

driver.find_element_by_css_selector('textarea#txtSource').send_keys('안녕하세요. 반갑습니다.')

time.sleep(2)
driver.close()
