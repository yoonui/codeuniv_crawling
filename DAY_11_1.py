# 동적 크롤링 2

from selenium import webdriver
import time


# 나만의 번역 사전 생성
my_dict = {}

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options)

papago_url = 'https://papago.naver.com/'
driver.get(papago_url)

time.sleep(2)


for i in range(3):
    question = input('번역할 영단어 입력: ')

    # 영단어를 파파고 페이지에 입력
    driver.find_element_by_css_selector('textarea#txtSource').send_keys(question)

    # 번역버튼 클릭
    driver.find_element_by_css_selector('button#btnTranslate').click()
    time.sleep(1)

    # 번역 결과 출력
    output = driver.find_element_by_css_selector('div#txtTarget').text
    my_dict[question] = output

    # 입력 칸 초기화
    driver.find_element_by_css_selector('textarea#txtSource').clear()


print(my_dict)

driver.close()
