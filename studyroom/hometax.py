from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 1. 크롬 접속
options = webdriver.ChromeOptions()
options.add_argument('--start-fullscreen')
driver = webdriver.Chrome('chromedriver', options=options)
driver.implicitly_wait(10)

# 2. 홈택스 접속
# 2.1 홈택스로 이동
url = 'https://hometax.go.kr/websquare/websquare_cdn.html?w2xPath=/ui/pp/index.xml'

driver.get(url)
driver.implicitly_wait(5)

# 2.2 로그인 화면으로 이동
driver.find_element(By.CSS_SELECTOR, '#textbox81212912').click()
time.sleep(2)

# 2.3 iframe 전환 : 로그인 화면은 화면전체가 iframe
iframe = driver.find_element(By.CSS_SELECTOR, '#txppIframe')
driver.switch_to.frame(iframe)
time.sleep(2)

driver.find_element(By.CSS_SELECTOR, '#group91882156.w2group').click()


# 2.4 id/pw 입력 후 로그인 버튼 클릭
driver.find_element(By.CSS_SELECTOR, '#iptUserId').send_keys('alrudsim')
driver.find_element(By.CSS_SELECTOR, '#iptUserPw').send_keys('#smk445566')
driver.find_element(By.CSS_SELECTOR, '#anchor25.w2anchor2.logingbtn').click()
time.sleep(3)

# 3. 조회/발급 메뉴 클릭
driver.find_element(By.CSS_SELECTOR, '#textbox81212923.w2textbox').click()
time.sleep(2)

# 3.1 iframe 전환
iframe = driver.find_element(By.CSS_SELECTOR, '#txppIframe')
driver.switch_to.frame(iframe)
time.sleep(2)

# 3.2 현금영수증조회 클릭
driver.find_element(By.CSS_SELECTOR, '#sub_a_0105010000.w2textbox').click()
# 3.2 매출내역 조회 클릭
driver.find_element(By.CSS_SELECTOR, '#sub_a_0105010600.w2textbox').click()
time.sleep(2)

# 4.1 주별 클릭
driver.find_element(By.CSS_SELECTOR, '#tabControl1_UTECRCB057_tab_tabs2').click()
time.sleep(5)

# 4.2 조회하기 클릭
driver.find_element(By.ID, 'trigger1').click()
time.sleep(2)

# 5.1 매출내역 항목 읽기
table = driver.find_element(By.ID, 'grdCshpt_body_tbody')

for tr in table.find_elements_by_tag_name("tr"):
    td = tr.find_elements_by_tag_name("td")
    #s = "{} , {} , {}\n".format(td[2].text, td[3].text, td[8].text)
    print (td[2].text, td[3].text, td[8].text)
    #fp.write(s)