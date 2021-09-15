# 라이브러리 csv _ csv 파일 읽기

import csv

# open() 함수를 사용하여 작성한 csv 파일 생성
# 파일 속 데이터를 읽어오는 것이므로 open() 함수의 읽기 옵션 r을 적용
f= open('./example.csv', 'r')

# CSV 파일을 읽기 위해 reader 객체를 사용
# reader 객체를 통해 파일의 모든 데이터를 읽어오고 변수 rdr에 저장
rdr = csv.reader(f)

# 열의 제목이 필요하지 않을 경우, 아래의 코드 사용
# next(rdr)

# 반복문을 사용하여 행별로 데이터를 출력
for row in rdr:
    print(row)

# 파일 닫기
f.close()
