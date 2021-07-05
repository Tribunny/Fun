'''

[task_local]
#湘创生活
0 9 * * * https://raw.githubusercontent.com/xl2101200/-/main/xcsh.js, tag=湘创生活
'''


import requests
import json
import os
from time import *


bg_time = time()

cookies1 = "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1aWQiOjEzMDQ5NTAsInNjb3BlIjo4LCJleHAiOjE2NTU4Njc1ODIsImlhdCI6MTYyNDMzMTU4Mn0.nMlHYTO9XHIvmO2nbbQJU1jPoCtur2h4CDwp4yxxJaA"

cookies2 = ""

cookiesList = [cookies1, ]   # 多账号准备

url = "https://api.csxcsh.com/api/sign/integral"

# ac读取环境变量
if "XCSHCK" in os.environ:
    xmly_speed_cookie = os.environ["XCSHCK"]
    cookiesList = []  # 重置cookiesList
    for v in xmly_speed_cookie.split('&'):
        if not v:
            continue
        cookiesList.append(v)


def main():
    cklen = len(cookiesList)
    print('🔔湘创生活签到, 开始!')
    print(f'共{str(cklen)}个账号')
    for i in range(cklen):
        print(f"=====第{i+1}个账号开始签到=====")
        sign(cookiesList[i])
        if i != cklen-1:
            sleep(2)
        print(f"=====第{i+1}个账号签到结束=====")

    print("=====签到任务结束=====")
    end_time = time()
    print("耗时%0.3f秒" % (end_time-bg_time))


def sign(cookie):
    header = {
        "log-header": "I am the log request header.",
        "Authorization": cookie,
        "Content-Length": "0",
        "Connection": "keep-alive",
        "Host": "api.csxcsh.com",
        "Accept-Encoding": "gzip",
        "User-Agent": "okhttp/3.12.6"
    }
    try:
        res = requests.post(url, headers=header, timeout=1000)
        res = json.loads(res.text)
        print(res['msg'], res['time'])
    except requests.exceptions.ConnectionError:
        print("连接错误,请检查网络！")


main()
