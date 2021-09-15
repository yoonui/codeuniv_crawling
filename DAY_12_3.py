# 라이브러리 csv _ 저장된 csv 파일에 행 추가

import csv

# 이미 존재하는 CSV 파일에 데이터를 추가
# open() 함수 사용 시, 추가 모드 옵션 a를 사용
f= open('./example.csv', 'a', newline='')

wtr = csv.writer(f)

wtr.writerow(['김감자','40','자바스크립트'])
wtr.writerow(['요하미','50','c#'])

# 파일 닫기
f.close()
