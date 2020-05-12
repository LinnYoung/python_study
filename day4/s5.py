#coding=utf-8

vec = [2,4,6]
val = [3*x for x in vec]
val3 = [3*x for x in vec if x >= 4]
print val, val3


val2 = [[x, "*2",x**2] for x in vec]
print val2

# strip()去掉字符串前后的空格
names = [' Linn ', 'mark' ,'LI xulu ']
print names
newName = [name.strip() for name in names]
print newName

#双重循环
vec1 = [2,4,6]
vec2 = [3,7,9]

vec12 = [x*y for x in vec1 for y in vec2]
print("vec12: ", vec12)


vec_12 = [vec1[i] * vec2[i] for i in range(len(vec1))]
#range(x) 0-x 的集合
print("len: ", len(vec1), range(len(vec1)))
print("vec_12: ", vec_12)
