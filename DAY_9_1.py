# 정적 크롤링 4

import requests
from bs4 import BeautifulSoup

keyword = input("뉴스 검색 키워드 : ")
count = 0

for page in range(1,11):
    # 단순히 page를 url 주소와 더해 주면 문자열+숫자 이므로 오류 발생
    # 반드시 str(page)로 작성
    new_url = 'https://search.hankyung.com/apps.frm/search.news?query=' + keyword + '&page=' + str(page)
    raw = requests.get(new_url)

    soup = BeautifulSoup(raw.text, 'html.parser')
    box = soup.find('ul', {'class':'article'})

    all_title = box.find_all('em', {'class':'tit'})

    print('< '+ str(page) + '페이지 뉴스 기사 제목 >')
    for title in all_title:
        count += 1
        t = title.text
        print(count, '-', t.strip()) # 문자열 앞뒤의 공백 제거
    print()
