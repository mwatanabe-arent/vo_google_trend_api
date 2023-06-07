from pytrends.request import TrendReq
import pandas as pd

import requests
from lxml import etree

#タイムゾーンとキーワード設定
trendReq = TrendReq(hl='ja-JP', tz=540)

trend_recent = trendReq.trending_searches(pn='japan')

print(trend_recent[0])
print(trend_recent[0][0])


kw_list = [trend_recent[0][0]]
trendReq.build_payload(kw_list=kw_list, timeframe='2023-05-24T15 2023-05-25T15', geo="JP")


relatedQueryResult = trendReq.related_queries()
print('-----RELATED QUERIES ------------')
print(relatedQueryResult)

print('-----Real time trends ------------')
realtime_trend = trendReq.realtime_trending_searches(pn='JP')
print(realtime_trend['title'])
print(realtime_trend['title'][5])

#for column_name in realtime_trend:
#    print(column_name)


#for title in realtime_trend['title']:
#    print(title)



#kw_list = [trend_recent[0][0]]

#地域別の数値
#trendReq.build_payload(kw_list=kw_list, timeframe='2023-05-24T15 2023-05-25T15', geo="JP")
#result = trendReq.interest_by_region(resolution='COUNTRY',inc_low_vol=True,inc_geo_code=True)
#print(result)

# 関連トピックの取得

topics = trendReq.related_topics()

#print(topics)
print('-------- topics -----------------')
for column_name in topics[kw_list[0]]['rising']:
    print(column_name)

print(topics[kw_list[0]]['rising']['link'][0])
print(topics[kw_list[0]]['rising'])

#print(topics[kw_list[0]]['rising'])

#print(topics[kw_list][0])
#print(topics[kw_list[0]]['rising'])

query = trendReq.related_queries()
#print (query)
for column_name in query[trend_recent[0][0]]:
    print(column_name)

print(query[trend_recent[0][0]]['top'])

#print(trend_recent.head())
#for column_name in trend_recent:
#    print(column_name)


#for index,data in trend_recent.iterrows():
    #print(index)
#    print(data[0])

