# 동적 크롤링 1

# 라이브러리 selenium : 웹 드라이버를 사용하여 자동화를 실현하는 라이브러리
# 사람이 데이터를 수집하는 방식 그대로 크롤링하는 기계를 만들어낸다.

# 라이브러리 time : 시간과 관련된 많은 함수를 제공하는 라이브러리
# 내장함수 sleep() : 각 작업 사이에 여유를 주면서 크롤링이 끊기지 않도록 설정함


from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options)

papago_url = 'https://papago.naver.com/'
driver.get(papago_url)

time.sleep(3)
driver.close()


## 동적 크롤링을 하기 위해 필요한 내장함수
# find_element_by_??() : 정적크롤링의 find()와 같은 역할
# 크롤링을 위해 HTML 요소를 찾는 함수

# find_elements_by_??() : 정적크롤링의 find_all() 함수와 같은 역할
# 입력한 태그 및 선택자에 해당하는 모든 HTML 요소를 찾는 함수

# click() : HTML 요소를 클릭하는 함수

# send_keys() : HTML 요소에 직접 텍스트를 입력하는 함수
# driver.find_element_by_??().send_keys('텍스트')
