import pandas as pd
from pygeocoder import Geocoder

lottemart = pd.read_csv('./서울특별시 롯데마트 위치정보.csv', encoding='CP949')
print(lottemart.columns)

emart = pd.read_csv('./서울특별시 이마트 위치정보.csv', encoding='CP949')
print(emart.columns)

costco = pd.read_csv('./서울특별시 코스트코 위치정보.csv', encoding='CP949')
print(costco.columns)

homeplus = pd.read_csv('./서울특별시 홈플러스 위치정보.csv', encoding='CP949')
print(homeplus.columns)


emart = emart[['지점명', '지번주소', '도로명주소', '점포유형']]


market = pd.DataFrame()
market = pd.concat( [market, lottemart] )
market = pd.concat( [market, emart] )
market = pd.concat( [market, costco] )
market = pd.concat( [market, homeplus] )

market.to_csv('./서울특별시 대형마트 위치정보.csv', index=False, encoding='CP949')
