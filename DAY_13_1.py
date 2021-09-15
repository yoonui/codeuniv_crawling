# 동적 크롤링 3 _ 첫번째 소스코드

# 영단어 번역 여러 번 실행
# 번역 결과를 모두 csv 파일에 저장

from selenium import webdriver
import time
import csv

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options)

papago_url = 'https://papago.naver.com/'
driver.get(papago_url)
time.sleep(2)

f = open('./my_papago.csv', 'w', newline='')
wtr = csv.writer(f)

wtr.writerow(['영단어','번역결과'])


# 무한 루프
while True:
    keyword = input('번역할 영단어 입력 (0 입력하면 종료): ')
    if keyword == '0':
        print('번역 종료')
        break

    # 영단어 입력, 번역 버튼 클릭
    driver.find_element_by_css_selector('textarea#txtSource').send_keys(keyword)
    driver.find_element_by_css_selector('button#btnTranslate').click()
    time.sleep(1)

    # 번역 결과 저장
    output = driver.find_element_by_css_selector('div#txtTarget').text

    # csv 파일에 [영단어, 번역결과] 작성
    wtr.writerow([keyword, output])

    # 영단어 입력 칸 초기화
    driver.find_element_by_css_selector('textarea#txtSource').clear()

# 크롬 창 닫기
driver.close()

# 파일 닫기
f.close()
