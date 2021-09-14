# 정적 크롤링 4 _ 문제

import requests
from bs4 import BeautifulSoup

keyward = input("뉴스 검색 키워드: ")
count = 0

for page in range(1,3):
    news_url = 'https://search.hankyung.com/apps.frm/search.news?query='+keyward+'&sort=DATE%2FDESC%2CRANK%2FDESC&period=ALL&area=ALL&mediaid_clust=HKPAPER&exact=&include=&except=&page='+str(page)
    raw = requests.get(news_url)

    soup = BeautifulSoup(raw.text, 'html.parser')

    box = soup.find('ul', {'class':'article'})

    # 뉴스 기사 제목
    all_title = box.find_all('em', {'class':'tit'})

    # 기사 작성 날짜 및 시간
    all_date = box.find_all('span', {'class':'date_time'})

    print('< ', str(page), ' 페이지 >')
    for title, date in zip(all_title, all_date):
        count+=1
        print(count, ' - [', date.text, '] : ', title.text.strip())
    print()
