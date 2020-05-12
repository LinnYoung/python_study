#coding=utf-8

#加了两个星号 ** 的参数会以字典的形式导入({a: 1, b:2})
# 一个星号 *的参数以 元组的形式导入
def add(*args):
    count = 0
    ite = iter(args)
    while True:
        try:
            count += ite.next()
        except Exception:
            return count

count = add(100,200,800)
print count
