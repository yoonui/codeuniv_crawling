# 동적 크롤링 5


from selenium import webdriver
import time

# 검색 키워드 입력
keyword = input('뉴스 검색 키워드 : ')

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options)

news_url = 'https://search.hankyung.com/apps.frm/search.news?query='+keyword+'&mediaid_clust=HKPAPER,HKCOM'
driver.get(news_url)
time.sleep(2)

# 모든 <em.tit> 태그를 변수에 저장
ten_articles = driver.find_elements_by_css_selector('em.tit')

# 단순히 뉴스마다 번호를 붙여주기 위한 변수
count = 0


# 뉴스 기사 제목을 클릭해서 기사 본문을 띄우면,
# 새로운 탭이 생기면서 뉴스 기사 본문을 보여준다.
# 직접 탭을 다루는 소스코드를 작성한다.
# driver.window_handles : 크롬 창에서 열린 탭을 모두 담고 있다.

# 새로운 탭이 켜지만, 보고있는 화면 창은 새로운 탭을 보여주지만,
# driver 변수는 여전히 기존에 켜져있는 탭을 나타낸다.
# 따라서 새로 켜진 탭에서 작업해야 한다면, driver 변수를 새로운 탭으로 전환
# driver.switch_to.window(작업할 탭)

# 10개의 뉴스 기사를 대상으로 반복문 실행
for article in ten_articles:
    # article은 뉴스 기사 제목을 나타내는 HTML 요소이므로, text는 제목을 나타낸다.
    title = article.text

    article.click()
    time.sleep(1)

    # driver를 새로운 새로운 탭(뉴스 기사 본문)으로 전환
    driver.switch_to.window(driver.window_handles[-1])
    
    # 기사 본문으로 content 변수에 저장
    content = driver.find_element_by_id('articletxt').text

    # content를 \n 단위로 나누어 seperate 변수에 저장
    seperate = content.split('\n')


    # 기사 본문 출력
    count += 1
    print(f'< {count}번 뉴스 - {title} >')

    for sep in seperate:
        # 아무것도 없는 공백이 포함되어 있기 때문에, 이런 공백은 출력하지 않음
        if sep != '':
            # 모든 sep 사이에 공백 한 칸을 삽입하여 출력
            print(sep, end = ' ')
    print('\n')

    # 새로운 탭에서 작업을 끝냈으므로, 새로운 탭은 닫아준다.
    driver.close()

    # 다시 driver를 처음 탭으로 전환
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(1)

driver.close()
