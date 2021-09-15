# 라이브러리 csv _ csv 파일 작성

# CSV는 Comma Separated Values의 약어로, 말 그대로 콤마(,)로 구분된다는 뜻이다.
# 따라서 CSV 파일은 콤마(,)로 구분한 텍스트 데이터 혹은 텍스트 파일을 뜻한다.
# CSV 파일의 확장자는 .csv이고, 보통 엑셀을 통해 CSV 파일을 확인할 수 있다.
# 한 줄이 하나의 행이 되고, 콤마(,)를 기준으로 열을 구분한다.


# CSV 파일을 다룰 수 있는 파이썬의 라이브러리 csv
# csv 라이브러리는 두 가지 객체 writer, reader를 사용하여 CSV 파일을 직접 작성하고 읽을 수 있다.


import csv

# open() 함수를 사용하여 csv 파일 생성
# newline 옵션을 통해 한 행씩 건너뛰면서 데이터가 작성되는 문제 해결
f= open('./example.csv', 'w', newline='')

# writer 객체를 사용하여 CSV 파일을 직접 작성
wtr = csv.writer(f)

# 파일 작성
wtr.writerow(['이름','나이','언어'])

# 데이터 생성
all_name = ['라츄','코딩맘','김콩순']
all_age = ['10','20','30']
all_language = ['c언어','자바','파이썬']

# 각 행에 데이터 작성
for i in range(3):
    name = all_name[i]
    age = all_age[i]
    language = all_language[i]
    wtr.writerow([name, age, language])

# 파일 닫기
f.close()
