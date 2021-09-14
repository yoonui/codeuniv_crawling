# 동적 크롤링 2 _ 문제

from selenium import webdriver
import time


my_dict = {}

def get_papago_result(question):
    driver.find_element_by_css_selector('textarea#txtSource').send_keys(question)

    driver.find_element_by_css_selector('button#btnTranslate').click()
    time.sleep(1)

    output = driver.find_element_by_css_selector('div#txtTarget').text

    # 입력칸 초기화
    driver.find_element_by_css_selector('textarea#txtSource').clear()

    return output


options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options)


url = 'https://papago.naver.com/'
driver.get(url)

time.sleep(3)


for i in range(5):
    question = input('번역할 영단어 입력 : ')
    my_dict[question] = get_papago_result(question)

print('번역 결과 : ', my_dict)


driver.close()
