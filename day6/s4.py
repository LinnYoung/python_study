#coding=utf-8
fo = open("foo.txt", "r+")
str = fo.read(10)
print "内容： ", str
fo.close()
