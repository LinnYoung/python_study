#coding=utf-8
import time
ticks = time.time()
print "当前时间戳： ",ticks
localTime = time.localtime(ticks)
#time.struct_time(tm_year=2020, tm_mon=5, tm_mday=9, tm_hour=18, tm_min=2, tm_sec=33, tm_wday=5, tm_yday=130, tm_isdst=0)

date = time.asctime(localTime)  # Sat May  9 18:05:58 2020
print "date： ",date

