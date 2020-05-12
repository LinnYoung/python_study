#coding=utf-8
a = 60  # 0011 1100
b = 13 #0000 1101
c = 0

c = a&b
print "one----c: " ,c # 12 (0000 1100)

c  = a|b
print "two ---c: ",c # 61（0011 1101）

c = a^b
print "three-----c: ", c # 49 （0011 0001） 16+32 +1 // 异或

c =~a;
print "four----c: ", a ,c #-61（加一 ，前面加一个负号）

c = ~b;
print "eight------c:", c

c = a<< 2;
print "five------c: ",c

c = a>>2;
print "six------c: ",c


c = b<< 2
print "seven ---- c: ",c






