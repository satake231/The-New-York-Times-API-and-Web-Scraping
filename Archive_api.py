import pandas as pd
import requests
#%%
api_endpoint = "https://api.nytimes.com/svc/archive/v1/2020/1.json?api-key=XKJP6DlmzSwBe5jGv8BaDs4An3Cgo1k1"

res = requests.get(api_endpoint)

print(res)
#%%
res_json = res.json()
#%%
print(res_json)
#%%
print(res_json.keys())
# copyright, response
#%%
print(res_json['copyright'])
#%%
print(res_json['response'].keys())
# docs, meta
#%%
print(res_json['response']['docs'])
# object type: list
#%%
print(res_json['response']['meta'])
# hits : 4480
#%%
n = 0
print(res_json['response']['docs'][n].keys())
# abstract, lead_paragraph, headline, keywords, news_desk, pub_date
#%%
print(res_json['response']['docs'][n]['web_url'])
#%%
print(res_json['response']['docs'][n]['abstract'])
#%%
print(res_json['response']['docs'][n]['lead_paragraph'])
#%%
print(res_json['response']['docs'][n]['pub_date'])
#%%
# リンクにアクセスした限りでは、どの部分に対応しているか不明
print(res_json['response']['docs'][n]['headline']['print_headline'])
#%%
# こっちがサイトでは見出しに使われている
print(res_json['response']['docs'][n]['headline']['main'])
#%%
print(res_json['response']['docs'][n]['keywords'][0]['value'])
print(len(res_json['response']['docs'][n]['keywords']))
# ここだけはループしてvalueだけリストか何かで抜き取る必要がある
#%%
print(res_json['response']['docs'][n]['news_desk'])
#%%
print(res_json['response']['docs'][n]['word_count'])
#%%
print(res_json['response']['docs'][n]['snippet'])
#%%
df = pd.DataFrame()
tmp_df = pd.DataFrame()
#%%
