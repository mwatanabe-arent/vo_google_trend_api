import requests
import json

subscription_key = "c76e37c678bb4c05b92a324a26103df4"
#search_url = "https://api.bing.microsoft.com/v7.0/search/"
search_url = "https://api.bing.microsoft.com/v7.0/news/search"
#search_url = "https://api.bing.microsoft.com/v7.0/news/trendingtopics"

ccCode = "JP"
search_query = "Sports"
freshness = "2019-02-01..2019-05-30"
#search_query = "politics"
#    "mkt":"en-US",

# cc United Kingdom > GB
# cc United State > US

headers = {"Ocp-Apim-Subscription-Key": subscription_key}
params = {
#    "cc":ccCode,
#    "q": search_query,
    "count":1,
#    "textDecorations": True, 
    "category":"LifeStyle",
#    "scene":"2015-01-01",
#    "freshness":"2022-12-01",
    "textFormat": "Raw"}

response = requests.get(search_url, headers=headers, params=params)
response.raise_for_status()
search_results = response.json()

print(search_results)

#print(search_results['webPages']['value'])

#for var in search_results['webPages']['value']:
#    print(var['name'])
#    print(var['url'])
#    print(var['snippet'])

