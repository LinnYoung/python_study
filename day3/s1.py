#!/usr/bin/python
# -*- coding: utf-8 -*-

# if基本用法
flag = False
name = 'luren'
if name == "python":
    flag = True
    print "welcome python!"
else:
    print "welcome: " + name


# if语句多个条件
num = 9
if num >= 0 and num <= 10:
    print "num 大于等于0 ， 小于等于10"
elif num < 0 or num > 10:
    print "小0 大 10"
else:
    print "其他"
