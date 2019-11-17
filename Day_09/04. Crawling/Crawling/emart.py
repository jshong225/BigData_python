import time
import requests
import pandas as pd
from bs4 import BeautifulSoup

url = 'https://store.emart.com/branch/list.do?trcknCode=header_store'

res = requests.get(url)
html = res.text
soup = BeautifulSoup(html, 'html.parser')

markets = soup.select('#branchList > li > a')


market_name = []
market_address_bunzi = []
market_address_load = []
url = "https://store.emart.com/branch/view.do?id={num}"

for market in markets:
    id = market['onclick'].replace("storeView('","").replace("'); return false;","")

    target = url.format(num=id)
    res = requests.get(target)

    html = res.text
    soup = BeautifulSoup(html, 'html.parser')

    addrs = soup.find_all("dd", {'class':'data'})

    market_name.append(market.text)
    for n, addr in enumerate(addrs):
        if n % 2 == 0:
            market_address_load.append(addr.text)
        else:
            market_address_bunzi.append(addr.text)

    time.sleep(0.5)

df = pd.DataFrame({
    '지점명' : market_name,
    '지번주소' : market_address_bunzi,
    '도로명주소' : market_address_load
})

df['지역구'] = df['지번주소'].str.slice(0,2,1)

df = df[df['지역구'] == '서울']
df['점포유형'] = '이마트'
df.to_csv('./서울특별시 이마트 위치정보.csv', index=False, encoding='CP949')