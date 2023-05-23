from pytrends.request import TrendReq
import pandas as pd

import requests
from lxml import etree


fileName = r"./Google検索年間ボリューム一覧.csv"

#タイムゾーンとキーワード設定
pytrends = TrendReq(hl='ja-JP', tz=540)

trend_recent = pytrends.trending_searches(pn='japan')


#print(trend_recent)
#print(trend_recent.head())
for column_name in trend_recent:
    print(column_name)


for index,data in trend_recent.iterrows():
    #print(index)
    print(data[0])

