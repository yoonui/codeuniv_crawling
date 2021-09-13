# 정적 크롤링 1

# requests 라이브러리의 get() 함수 : 웹 페이지의 내용을 요청하는 함수
# 함수의 입력 변수로 웹 주소(url)를 사용한다.

import requests

lotto_url = 'https://dhlottery.co.kr/gameResult.do?method=byWin'
raw = requests.get(lotto_url)

print(raw.text)
