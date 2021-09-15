# 동적 크롤링 3 _ 두번째 소스코드

# 영단어 번역 여러 번 실행
# csv 파일에 있는 영단어일 경우, 저장하지 않음
# csv 파일에 없는 영단어는 번역 결과 저장


from selenium import webdriver
import time
import csv

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options)

papago_url = 'https://papago.naver.com/'
driver.get(papago_url)
time.sleep(2)

f = open('./my_papago.csv', 'r')
rdr = csv.reader(f)

# rdr의 첫번째(열 제목)는 건너뜀
next(rdr)


# 불러온 데이터를 딕셔너리로 저장
my_dict = {}

# 딕셔너리에 영단어와 번역 결과를 모두 저장
for row in rdr:
    keyword = row[0]
    korean = row[1]
    my_dict[keyword] = korean

f.close()


# 새로운 번역 결과를 추가로 저장하기 위해 추가 옵션 'a'를 사용하여 열어준다.
f = open('./my_papago.csv', 'a', newline='')
wtr = csv.writer(f)


# 무한 루프
while True:
    keyword = input('번역할 영단어 입력 (0 입력하면 종료): ')
    if keyword == '0':
        print('번역 종료')
        break

    # 영단어가 my_dict의 키 값 중에 있다면, 이 사실을 알려주고 저장되어있던 번역 결과 출력
    if keyword in my_dict.keys():
        print('이미 번역한 영단어 입니다. 뜻은 ', my_dict[keyword], ' 입니다.')
    else:
        driver.find_element_by_css_selector('textarea#txtSource').send_keys(keyword)
        driver.find_element_by_css_selector('button#btnTranslate').click()
        time.sleep(1)

        output = driver.find_element_by_css_selector('div#txtTarget').text

        # CSV 파일에 행 추가
        wtr.writerow([keyword, output])

        # 딕셔너리에 추가
        my_dict[keyword] = output
        
        driver.find_element_by_css_selector('textarea#txtSource').clear()

# 크롬 창 닫기
driver.close()

# 파일 닫기
f.close()
