import requests

loginurl="http://vipmusic.1tai.com/boss/admin/auth/signin"
fake_sms="http://vipmusic.1tai.com/boss/admin/user/fake_sms"

logindata={
     "username":"libing",
     "pwd":"123456"

}

requespond=requests.post(loginurl,data=logindata)
vipcookie=requespond.cookies
# print(requespond.text)
# print(requespond.cookies)

smsdata={
    "mobile":"15810318261"

}

re_sms=requests.post(fake_sms,data=smsdata,cookies=vipcookie)
print(re_sms.text)