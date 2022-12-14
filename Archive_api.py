import requests

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
n = 0
print(res_json['response']['docs'][n].keys())
# abstract, lead_paragraph, headline, keywords, news_desk, section_name
#%%
print(res_json['response']['docs'][n]['abstract'])
#%%
print(res_json['response']['docs'][n]['lead_paragraph'])
#%%
print(res_json['response']['docs'][n]['headline']['print_headline'])
#%%
print(res_json['response']['docs'][n]['keywords'][0]['value'])
# ここだけはループしてvalueだけ抜き取る必要がある
#%%
print(res_json['response']['docs'][n]['news_desk'])
