#coding=utf-8
# count = 0
# while (count < 9):
#     print "count: ",count
#     count += 1

# print('跳出循环')

#continue and break 用法

i = 1
while i < 10:
    i+=1
    if i%2>0:
        continue
    print i

i = 1
while 1: #循环条件为1必定成立
    print i
    i+=1
    if i>10:
        break
