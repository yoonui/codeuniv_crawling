# 정적 크롤링 2

# 크롤링을 위해서는 단순히 문자열을 다루는 것이 아닌, 실제 HTML 코드를 다뤄야 한다.
# BeautifulSoup 라이브러리는 텍스트 결과를 실제 HTML 코드로 변환

from bs4 import BeautifulSoup
# bs4 라이브러리에서 BeautifulSoup 메소드만 가져와서 사용

import requests

lotto_url = 'https://dhlottery.co.kr/gameResult.do?method=byWin'
raw = requests.get(lotto_url)

soup = BeautifulSoup(raw.text, 'html.parser')

# find_all() : HTML 코드에서 원하는 부분을 가져오는 함수
# 원하는 부분을 지정할 때 사용하는 것이 '태그'와 '선택자'
# find_all()은 HTML 코드를 리스트 형태로 반환한다.

# find() : find_all() 함수는 원하는 모든 것을 가져오지만, find() 함수는 딱 하나만 가져온다.

box = soup.find('div', {'class':'nums'})
numbers = box.find_all('span')

for number in numbers:
    print(number.text) # 텍스트 데이터로 출력
