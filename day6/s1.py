#coding=utf-8

# raw_input([prompt]) 函数从标准输入读取一个行，并返回一个字符串（去掉结尾的换行符）
inputStr = raw_input("Please input your name: ")
print "Hello",inputStr


#input([prompt]) 函数和 raw_input([prompt]) 函数基本类似，但是 input 可以接收一个Python表达式作为输入，并将运算结果返回

# input2 = input("Please input: ")
# print input2
# [x*3 for x in [2,4,6]]
# [6, 12, 1]

lll = [x  for x in range(2,10,2)]
print lll

jjj = range(2,10,2) # 从2开始 到9  步长 2 【 2 ， 2+2 ， 2+2+2， 2+2+2+2】
print jjj
