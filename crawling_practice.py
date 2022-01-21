import requests
from bs4 import BeautifulSoup as bs  # Requests로 받아온 데이터를 파이썬이 이해하는 객체로 만들기, HTML DOM 구조로 가져옴

# Get 방식으로 소스를 가져옴
r = requests.get('https://www.pycon.kr/2017/program/list/')
# 헤더부분이 아닌 HTTP의 Body(Text)를 가져옴
html = r.text
# HTML을 파이썬이 이해하는 Soup 객체로 파싱
soup = bs(html, 'html.parser')
# CSS Selector를 통해 내용물을 모두 선택(Iterable)
session_list = soup.select('div > div.col-md-9.content > ul > li > a')

for session in session_list:
    print(session)
