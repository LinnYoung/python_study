#coding=utf-8
import time
localeTime = time.localtime()

#格式化成 2020-05-09 18：09：13

date =  time.strftime("%Y-%m-%d %H:%M:%S",localeTime)
print date
timeStap = time.mktime(time.strptime(date, "%Y-%m-%d %H:%M:%S"))

print timeStap
