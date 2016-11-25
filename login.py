import requests
import os
url = "http://172.18.6.30/eportal/userV2.do"
username = os.getenv("USER_NAME_LOGNET")
pwd      = os.getenv("PWD_LOGNET")
params = {
    "method": "login",
    "param": "true",
    "wlanuserip": "3d657ded63206c6698cc3b4f5bef19f2",
    "wlanacname": "353477f414861cdd",
    "ssid": "15e792de8d103cfd",
    "nasip": "704b71fc82aa0c88911e9f71944eba43",
    "mac": "aad9ba78888755209ff8e82016aa5765",
    "t": "wireless-v2",
    "url": "d6c902208565460ca83f36f84b7ea3874c9c9ad789327c75",
    "username": username,
    "pwd": pwd,
}
data = {
    "usernameHidden": "2014216475",
    "username": "2014216475",
    "authorMode": "",
    "pwd": "723535"
}
r = requests.post(url=url, data=data, params=params)
r.encoding = "GBK"
print(r.status_code)

