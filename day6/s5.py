#coding=utf-8
fo = open("foo.txt", 'r+')

str = fo.read(10)
print str

position = fo.tell()
print "position : ", position

position = fo.seek(0,0)
print "llll: ", position

str = fo.read(5)
print str

position = fo.tell()
print  position

fo.close()
