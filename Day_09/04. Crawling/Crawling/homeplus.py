import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome('./chromedriver.exe')

driver.get('http://corporate.homeplus.co.kr/STORE/HyperMarket.aspx')

driver.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_Region_Code"]/option[2]').click()

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')


markets = soup.select('#content > div > div > div > ul > li > div > h3 > span.name > a')

market_name = []
market_address_bunzi = []
market_address_load = []

for market in markets:
    market_name.append(market.text)

    url = 'http://corporate.homeplus.co.kr' + market['href']
    res = requests.get(url)
    html = res.text
    soup = BeautifulSoup(html, 'html.parser')

    addrs = soup.select('#store_detail01 > table > tbody > tr > td')

    market_address_load.append(addrs[0].text)
    market_address_bunzi.append('')


df = pd.DataFrame({
    '지점명' : market_name,
    '지번주소' : market_address_bunzi,
    '도로명주소' : market_address_load
})

df['점포유형'] = '홈플러스'

df.to_csv('./서울특별시 홈플러스 위치정보.csv', index=False, encoding='CP949')


