import requests
url = "http://172.18.6.30/eportal/userV2.do"
params = {
    "method": "offlineAcct",
}
r = requests.get(url=url, params=params)
r.encoding = "GBK"
print(r.status_code)

