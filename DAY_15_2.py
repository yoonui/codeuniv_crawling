# 동적 크롤링 5 _ 문제


from selenium import webdriver
import time

keyword = input('뉴스 검색 키워드 : ')


options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options)

news_url = 'https://search.hankyung.com/apps.frm/search.news?query='+keyword+'&mediaid_clust=HKPAPER,HKCOM'
driver.get(news_url)
time.sleep(2)


ten_articles = driver.find_elements_by_css_selector('em.tit')

count = 0
for i in range(1,4):
    # 10개의 뉴스기사를 대상으로 반복문 실행
    for article in ten_articles:
        title = article.text

        article.click()
        time.sleep(1)

        driver.switch_to.window(driver.window_handles[-1])
        content = driver.find_element_by_id('articletxt').text

        seperate = content.split('\n')

        count += 1
        print(f'< {count}번 뉴스 - {title} >')

        for sep in seperate:
            if sep != '':
                print(sep, end = ' ')
        print('\n')

        driver.close()

        driver.switch_to.window(driver.window_handles[0])
        time.sleep(1)

    driver.find_element_by_xpath('//*[@id="content"]/div[1]/div[2]/div[2]/div/span/a['+str(i)+']')

driver.close()
