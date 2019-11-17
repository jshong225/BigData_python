import time
import requests
import pandas as pd
from bs4 import BeautifulSoup

url = 'http://company.lottemart.com/bc/branchSearch/branchSearch.do?currentPageNo={num}&schRegnCd=BC0101'

market_name = []
market_address_bunzi = []
market_address_load = []

for num in range(1,7):
    target = url.format(num=num)

    res = requests.get(target)

    html = res.text
    soup = BeautifulSoup(html, 'html.parser')

    names = soup.select('#contents > ul > li > div > div.article1 > h3')

    for name in names:
        market_name.append(name.text)

    addrs = soup.select('#contents > ul > li > div > div.article2 > ul > li ')

    for n, addr in  enumerate(addrs):
        if n % 2 == 0:
            market_address_load.append(str(addr.text)[1:])
        else:
            market_address_bunzi.append(str(addr.text)[1:])
    time.sleep(1)


df = pd.DataFrame({
    '지점명' : market_name,
    '지번주소' : market_address_bunzi,
    '도로명주소' : market_address_load
})

df['점포유형'] = '롯데마트'
df.to_csv('./서울특별시 롯데마트 위치정보.csv', index=False, encoding='CP949')