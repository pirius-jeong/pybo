from selenium import webdriver
import time

# 1. 크롬 접속
driver = webdriver.Chrome()
driver.implicitly_wait(20)

# 2. 홈택스 접속
# 2.1 홈택스로 이동
url = 'https://hometax.go.kr/websquare/websquare_cdn.html?w2xPath=/ui/pp/index.xml'
driver.get(url)
driver.implicitly_wait(10)

# 2.2 로그인 화면으로 이동
driver.find_element_by_css_selector('#textbox81212912').click()
time.sleep(3)

# 2.3 iframe 전환 : 로그인 화면은 화면전체가 iframe
iframe = driver.find_element_by_css_selector('#txppIframe')
driver.switch_to.frame(iframe)
time.sleep(3)

driver.find_element_by_css_selector('#group91882156.w2group').click()


# 2.4 id/pw 입력 후 로그인 버튼 클릭
driver.find_element_by_css_selector('#iptUserId').send_keys('alrudsim')
driver.find_element_by_css_selector('#iptUserPw').send_keys('#smk445566')
driver.find_element_by_css_selector('#anchor25.w2anchor2.logingbtn').click()
time.sleep(3)