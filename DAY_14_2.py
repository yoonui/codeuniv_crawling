# 동적 크롤링 4 _ 문제


from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options)

login_url = 'https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com'
driver.get(login_url)
time.sleep(2)


my_id= # 아이디
my_pw= # 비밀번호

driver.execute_script("document.getElementsByName('id')[0].value = \'" + my_id + "\'")
driver.execute_script("document.getElementsByName('pw')[0].value = \'" + my_pw + "\'")
time.sleep(1)

driver.find_element_by_id('log.login').click()
time.sleep(1)

codeuniv_url = 'https://cafe.naver.com/codeuniv'
driver.get(codeuniv_url)
time.sleep(2)

driver.find_element_by_id('menuLink90').click()
time.sleep(1)


driver.switch_to.frame('cafe_main') # 프레임 전환
time.sleep(1)

driver.find_element_by_xpath('//*[@id="main-area"]/div[4]/table/tbody/tr[1]/td[1]/div[2]/div/a').click()
time.sleep(1)


for i in range(1, 21):
    # 글 내용 출력
    content = driver.find_element_by_css_selector('div.se-component-content').text
    print('< ', i, '번째 게시물 >')
    print(content)
    if i == 1:
        driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/div[2]/a[1]').click()
    else:
        driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/div[2]/a[2]').click()
    time.sleep(1)
    
driver.close()
