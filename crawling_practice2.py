from selenium import webdriver

# 크롬드라이버 다운받은걸 명시
driver = webdriver.Chrome('/home/mingyeong/Downloads/chromedriver_linux64/chromedriver')
# Selenium 이 모든 자원을 가져오기까지 3초를 기다려줌
driver.implicitly_wait(3)
# 네이버 첫 화면
driver.get('https://naver.com')
