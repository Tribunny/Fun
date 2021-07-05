"""
抓取header中的cookie，
只需要取SSO-SESSION-ID和UFO-SESSION-ID两个参数
添加环境变量
export LDYGOCK = "第一个账号&第二个账号&···"
每个账号的ck格式
SSO-SESSION-ID=xxxxx; UFO-SESSION-ID=xxxxx;

[task_local]
#联动云
0 9 * * * https://raw.githubusercontent.com/Tribunny/Fun/main/ldygo.py, tag=联动云, enabled=true
"""


import requests
import datetime
import time
import json
import os


bg_time = time.time()

cookies1 = ""

cookies2 = ""

cookiesList = [cookies1, ]   # 多账号准备

url = "https://m.ldygo.com/los/zuche-intf-union.signIn"

# ac读取环境变量
if "LDYGOCK" in os.environ:
    ldygo_speed_cookie = os.environ["LDYGOCK"]
    cookiesList = []  # 重置cookiesList
    for v in ldygo_speed_cookie.split('&'):
        if not v:
            continue
        cookiesList.append(v)


def main():
    cklen = len(cookiesList)
    print('🔔联动云签到, 开始!')
    print(f'共{str(cklen)}个账号')
    for i in range(cklen):
        print(f"=====第{i + 1}个账号开始签到=====")
        sign(cookiesList[i])
        if i != cklen - 1:
            time.sleep(2)
        print(f"=====第{i + 1}个账号签到结束=====")

    print("=====签到任务结束=====")
    end_time = time.time()
    print("耗时%0.3f秒" % (end_time - bg_time))


def sign(cookie):
    dtime = datetime.datetime.now()
    un_time = int(time.mktime(dtime.timetuple()))
    data = {"_channel_id": "02", "_client_version_no": "2.16.0", "timestamp": un_time}
    header = {
         "Cookie": cookie
    }
    try:
        res = requests.post(url, headers=header, data=data, timeout=1000)
        res = json.loads(res.text)
        if res['responseCode'] == "000000":
            print(f"签到成功！获得{res['model']['points']}个☁")
        else:
            print(f"签到失败！{res['responseMsg']}")
    except requests.exceptions.ConnectionError:
        print("连接错误,请检查网络！")


main()
