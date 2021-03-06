# 동적 크롤링 4

# 코뮤니티 카페에 접속해서 '신규회원게시판'에 작성된 게시물의 내용을 수집


from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options)

login_url = 'https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com'
driver.get(login_url)
time.sleep(2)


# 네이버는 자동화된 소프트웨어를 막기 때문에,
# send_keys() 함수를 사용하여 로그인하면 자동입력방지기능이 나타난다.
# 따라서 selenium의 execute_script() 함수를 사용하여 로그인한다.
my_id= # 아이디
my_pw= # 비밀번호

driver.execute_script("document.getElementsByName('id')[0].value = \'" + my_id + "\'")
driver.execute_script("document.getElementsByName('pw')[0].value = \'" + my_pw + "\'")
time.sleep(1)

# 로그인 버튼 클릭
driver.find_element_by_id('log.login').click()
time.sleep(1)

# 코뮤니티 접속
codeuniv_url = 'https://cafe.naver.com/codeuniv'
driver.get(codeuniv_url)
time.sleep(2)

# '신규회원게시판' 클릭
driver.find_element_by_id('menuLink90').click()
time.sleep(1)


# 프레임 : 웹페이지의 HTML 안에 또다른 HTML을 넣어둔 것
driver.switch_to.frame('cafe_main') # 프레임 전환
time.sleep(1)

# 첫번째 글 클릭 - 첫번째 게시물의 XPath
driver.find_element_by_xpath('//*[@id="main-area"]/div[4]/table/tbody/tr[1]/td[1]/div[2]/div/a').click()
time.sleep(1)

content = driver.find_element_by_css_selector('div.se-component-content').text
print(content)

driver.close()
