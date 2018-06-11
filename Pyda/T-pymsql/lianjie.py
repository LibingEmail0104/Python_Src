#encoding=utf-8

import pymysql
import json
import sys

print(sys.getdefaultencoding())

#创建连接=服务器地址、用户名、密码、数据库
db= pymysql.connect(host='52.80.176.253',port=3606,user='xiaoyezi',passwd='xiaoyezi456',db='test')

#创建游标
cursor=db.cursor(cursor=pymysql.cursors.DictCursor)

#执行

sql="select * from user where mobile ='18346069584'"
reCount=cursor.execute(sql)
reData=cursor.fetchall()


print(reData)

#print(json.dumps(reData,ensure_ascii=False))



print("SQL")

print("ewfwf")