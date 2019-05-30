
"""
发送带有附件的邮件
"""

import urllib.parse
import http.client
import json

def main():
    host = '106.ihuyi.com'
    sms_send_url = '/webservice/sms.php?method=Submit'
    # 下面的参数需要填入自己注册的账号和对应的密码
    param = urllib.parse.urlencode({'account': 'your account', 'password' : 'your pass', 'content': 'your code is：147258。xxxxxxxxxx。', 'mobile': 'receiver mobile', 'format':'json' })
    print(param)
    headers = {'Content-type': 'application/x-www-form-urlencoded', 'Accept': 'text/plain'}
    conn = http.client.HTTPConnection(host, port=80, timeout=30)
    conn.request('Post',sms_send_url,param,headers)
    res = conn.getresponse()
    res_str = res.read()
    jsonStr = res_str.decode('utf-8')
    print(json.loads(jsonStr))
    conn.close()


if __name__ == '__main__':
    main()