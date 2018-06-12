# coding:utf-8

import os
import time

files = os.listdir("/Users/xiaoyezi/Desktop/works/安装包/Android")

devices=os.popen("adb devices")
print(devices.read())

for i in files:
    print("adb install "+i)

    text_log = os.popen("adb install -r /Users/xiaoyezi/Desktop/works/安装包/Android/"+i)
    time.sleep(10)
    print( text_log.read())