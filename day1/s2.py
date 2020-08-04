#coding=utf-8
#多变量赋值
# a = b = c =1
# print(a," ",b, " ",c)
# a ,b,c = 1,2,"linn";
# print(a," ",b, " ",c)

'''
    Python 定义了一些标准类型，用于存储各种类型的数据。

    Python有五个标准的数据类型：

    Numbers（数字）
        Python支持四种不同的数字类型：

        int（有符号整型）
        long（长整型[也可以代表八进制和十六进制]）
        float（浮点型）
        complex（复数）
        实例
        一些数值类型的实例：

    int	    long	    float	    complex
    10	    51924361L	0.0	        3.14j
    100	    -0x19323L	15.20	    45.j
    -786	0122L	    -21.9	    9.322e-36j
    080	  0xDEFABCECBDAECBFBAEl	32.3e+18	.876j
    -0490	535633629843L	-90.	-.6545+0J
    -0x260	-052318172735L	-32.54e100	3e+26J
    0x69	-4721885298529L	70.2E-12	4.53e-7j
长整型也可以使用小写 l，但是还是建议您使用大写 L，避免与数字 1 混淆。Python使用 L 来显示长整型。
Python 还支持复数，复数由实数部分和虚数部分构成，可以用 a + bj,或者 complex(a,b) 表示， 复数的实部 a 和虚部 b 都是浮点型


    String（字符串）
    List（列表）
    Tuple（元组）
    Dictionary（字典）

'''


val = 12
val2 = 'linn'
print(val, val2)

del val #删除引用
val = "Young"
print(val+val2)
