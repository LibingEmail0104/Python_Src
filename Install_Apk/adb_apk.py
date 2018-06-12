# coding:utf-8

import os
import time

#文件路径
paths="/Users/xiaoyezi/Desktop/works/安装包/Android/"
files = os.listdir(paths)

#查看连接设备名称
devices=os.popen("adb devices")
print(devices.read())

#遍历并且安装
# for i in files:
#     print("adb install "+i)
#
#     text_log = os.popen("adb install -r /Users/xiaoyezi/Desktop/works/安装包/Android/"+i)
#     time.sleep(10)
#     print( text_log.read())

#通过用户指定安装
for i in files:
    print("adb install "+i)

apk=input("请输入需要安装的安装包名称：")

text_log = os.popen("adb install -r "+paths+apk)
print(text_log.read())

