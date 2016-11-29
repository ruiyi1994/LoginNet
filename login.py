import requests
import os
url = "http://172.18.3.3"
username = os.getenv("USERNAME_LOGNET")
pwd = os.getenv("PWD_LOGNET")
data = {
    "DDDDD": username,
    "upass": pwd,
    "R1": "0",
    "R2": "1",
    "para": "00",
    "0MKKey": "123456"
}
r = requests.post(url=url, data=data)
r.encoding = "gb2312"
print(r.status_code)

