# 동적 크롤링 4

# 코뮤니티 카페에 접속해서 '신규회원게시판'에 작성된 게시물의 내용을 수집

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options)

url = 'https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com'
driver.get(url)
time.sleep(2)


# 네이버는 자동화된 소프트웨어를 막기 때문에,
# send_keys() 함수를 사용하여 로그인하면 자동입력방지기능이 나타난다.
# 따라서 selenium의 execute_script() 함수를 사용하여 로그인

