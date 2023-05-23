
kw_list =["乾燥機", "冷蔵庫","エアコン","テレビ","体重計"]

#データ作成
pytrends.build_payload(kw_list, cat=0, timeframe='2021-01-01 2021-12-31', geo='JP', gprop='')

#データ取得
df = pytrends.interest_over_time()

for kw in kw_list:
   google_r = requests.get("http://www.google.com/complete/search",
                 params={'q':kw,
                         'hl':'ja',
                         'ie':'utf_8',
                         'oe':'utf_8',
                         'output': 'toolbar'})

   google_root = etree.XML(google_r.text)
   google_sugs = google_root.xpath("//suggestion")
   google_sugstrs = [s.get("data") for s in google_sugs]

   google_suglist = []

   for ss in google_sugstrs:
       google_suglist.append(ss)
       #print(ss)