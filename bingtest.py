import requests
import json

subscription_key = "c76e37c678bb4c05b92a324a26103df4"
search_url = "https://api.bing.microsoft.com/v7.0/search/"
search_url = "https://api.bing.microsoft.com/v7.0/news/search"
search_term = "野球"

headers = {"Ocp-Apim-Subscription-Key": subscription_key}
params = {"q": search_term, "textDecorations": True, "textFormat": "Raw","count":1}

response = requests.get(search_url, headers=headers, params=params)
response.raise_for_status()
search_results = response.json()

print(search_results)

#print(search_results['webPages']['value'])

#for var in search_results['webPages']['value']:
#    print(var['name'])
#    print(var['url'])
#    print(var['snippet'])

