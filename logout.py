import requests
url = "http://172.18.3.3/F.htm"
r = requests.get(url=url)
r.encoding = "gb2312"
print(r.status_code)

