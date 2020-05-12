#coding=utf-8

tuple = ('runoob', 789, 2.31, 'john', 70.2)

# tinytuple = (123, 'linn')

# print tuple
# print tuple[0]
# print tuple[1:3]
# print tuple[2:]
# print tinytuple * 2
# print tuple + tinytuple

list = ['runoob', 789, 2.31, 'john', 70.2]

#以下是元组无效的，因为元组是不允许更新的。而列表是允许更新的
# tuple[2] = 000 #元组中是非法应用
list[2] = 000
print(tuple , list)
