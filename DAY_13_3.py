# 동적 크롤링 3 _ 문제

from selenium import webdriver
import time
import csv

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options)

papago_url = 'https://papago.naver.com/'
driver.get(papago_url)
time.sleep(2)

driver.find_element_by_css_selector('button.btn_switch___x4Tcl.disable___1r5H-').click()


f = open('./my_papago.csv', 'r')
rdr = csv.reader(f)

next(rdr)


for row in rdr:
    driver.find_element_by_css_selector('textarea#txtSource').send_keys(row[1])
    driver.find_element_by_css_selector('button#btnTranslate').click()
    time.sleep(1)

    output = driver.find_element_by_css_selector('div#txtTarget').text
    print('번역 결과는 ', output, ' 입니다.')
    
    driver.find_element_by_css_selector('textarea#txtSource').clear()

# 크롬 창 닫기
driver.close()

# 파일 닫기
f.close()
