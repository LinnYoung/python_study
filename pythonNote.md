下面的列表显示了在 Python 中的保留字。这些保留字不能用作常数或变数，或任何其他标识符名称。

所有 Python 的关键字只包含小写字母。

and exec not
assert finally or
break for pass
class from print
continue global raise
def if return
del import try
elif in while
else is with
except lambda yield

python 中多行注释使用三个单引号(''')或三个双引号(""")。

Python 定义了一些标准类型，用于存储各种类型的数据。

Python 有五个标准的数据类型：
Numbers（数字）
String（字符串）
List（列表）
Tuple（元组）
Dictionary（字典）

     Python支持四种不同的数字类型：
        int（有符号整型）
        long（长整型[也可以代表八进制和十六进制]）
        float（浮点型）
        complex（复数）

python 的字串列表有 2 种取值顺序:
从左到右索引默认 0 开始的，最大范围是字符串长度少 1
从右到左索引默认-1 开始的，最大范围是字符串开头

Python 元组
元组是另一个数据类型，类似于 List（列表）。

元组用 () 标识。内部元素用逗号隔开。但是元组不能二次赋值，相当于只读列表

**\*\***\*\*\***\*\***.数据类型转换

有时候，我们需要对数据内置的类型进行转换，数据类型的转换，你只需要将数据类型作为函数名即可。

以下几个内置的函数可以执行数据类型之间的转换。这些函数返回一个新的对象，表示转换的值。

函数 描述
int(x [,base]) 将 x 转换为一个整数

long(x [,base] ) 将 x 转换为一个长整数

float(x) 将 x 转换到一个浮点数

complex(real [,imag]) 创建一个复数

str(x) 将对象 x 转换为字符串

repr(x) 将对象 x 转换为表达式字符串

eval(str) 用来计算在字符串中的有效 Python 表达式,并返回一个对象

tuple(s) 将序列 s 转换为一个元组

list(s) 将序列 s 转换为一个列表

set(s) 转换为可变集合

dict(d) 创建一个字典。d 必须是一个序列 (key,value)元组。

frozenset(s) 转换为不可变集合

chr(x) 将一个整数转换为一个字符

unichr(x) 将一个整数转换为 Unicode 字符

ord(x) 将一个字符转换为它的整数值

hex(x) 将一个整数转换为一个十六进制字符串

oct(x) 将一个整数转换为一个八进制字符串

---------------------运算符-------------------------

运算符 描述 实例

- 加 - 两个对象相加 a + b 输出结果 30

* 减 - 得到负数或是一个数减去另一个数 a - b 输出结果 -10

- 乘 - 两个数相乘或是返回一个被重复若干次的字符串 a \* b 输出结果 200

/ 除 - x 除以 y b / a 输出结果 2

% 取模 - 返回除法的余数 b % a 输出结果 0

** 幂 - 返回 x 的 y 次幂 a**b 为 10 的 20 次方， 输出结果 100000000000000000000

// 取整除 - 返回商的整数部分（向下取整）

> > > 9//2
> > > 4
> > > -9//2
> > > -5

**\*\*\***位运算符

    运算符	描述	实例

& 按位与运算符：参与运算的两个值,如果两个相应位都为 1,则该位的结果为 1,否则为 0 (a & b) 输出结果 12 ，二进制解释： 0000 1100
| 按位或运算符：只要对应的二个二进位有一个为 1 时，结果位就为 1。 (a | b) 输出结果 61 ，二进制解释： 0011 1101
^ 按位异或运算符：当两对应的二进位相异时，结果为 1 (a ^ b) 输出结果 49 ，二进制解释： 0011 0001
~ 按位取反运算符：对数据的每个二进制位取反,即把 1 变为 0,把 0 变为 1 。~x 类似于 -x-1 (~a ) 输出结果 -61 ，二进制解释： 1100 0011，在一个有符号二进制数的补码形式。
<< 左移动运算符：运算数的各二进位全部左移若干位，由 << 右边的数字指定了移动的位数，高位丢弃，低位补 0。 a << 2 输出结果 240 ，二进制解释： 1111 0000

> >     右移动运算符：把">>"左边的运算数的各二进位全部右移若干位，>> 右边的数字指定了移动的位数	a >> 2 输出结果 15 ，二进制解释： 0000 1111

*********运算符优先级********
**	指数 (最高优先级)
~ + -	按位翻转, 一元加号和减号 (最后两个的方法名为 +@ 和 -@)
* / % //	乘，除，求余数和取整除
+ -	加法减法
>> <<	右移，左移运算符
&	位 'AND'
^ |	位运算符
<= < > >=	比较运算符
== !=	等于运算符
= %= /= //= -= += *= **=	赋值运算符
is is not	身份运算符
in not in	成员运算符
not and or	逻辑运算符

#
序号	函数
1	cmp(list1, list2)
    比较两个列表的元素
2	len(list)
    列表元素个数
3	max(list)
    返回列表元素最大值
4	min(list)
    返回列表元素最小值
5	list(seq)
    将元组转换为列表

Python包含以下方法:
序号	方法
1	list.append(obj)
    在列表末尾添加新的对象
2	list.count(obj)
    统计某个元素在列表中出现的次数
3	list.extend(seq)
    在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
4	list.index(obj)
    从列表中找出某个值第一个匹配项的索引位置
5	list.insert(index, obj)
    将对象插入列表
6	list.pop([index=-1])
    移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
7	list.remove(obj)
    移除列表中某个值的第一个匹配项
8	list.reverse()
    反向列表中元素
9	list.sort(cmp=None, key=None, reverse=False)
    对原列表进行排序

************时间*************
%y 两位数的年份表示（00-99）
%Y 四位数的年份表示（000-9999）
%m 月份（01-12）
%d 月内中的一天（0-31）
%H 24小时制小时数（0-23）
%I 12小时制小时数（01-12）
%M 分钟数（00=59）
%S 秒（00-59）
%a 本地简化星期名称
%A 本地完整星期名称
%b 本地简化的月份名称
%B 本地完整的月份名称
%c 本地相应的日期表示和时间表示
%j 年内的一天（001-366）
%p 本地A.M.或P.M.的等价符
%U 一年中的星期数（00-53）星期天为星期的开始
%w 星期（0-6），星期天为星期的开始
%W 一年中的星期数（00-53）星期一为星期的开始
%x 本地相应的日期表示
%X 本地相应的时间表示
%Z 当前时区的名称
%% %号本身

*****************open*******
open 函数
你必须先用Python内置的open()函数打开一个文件，创建一个file对象，相关的方法才可以调用它进行读写。

语法：

file object = open(file_name [, access_mode][, buffering])
各个参数的细节如下：

file_name：file_name变量是一个包含了你要访问的文件名称的字符串值。
access_mode：access_mode决定了打开文件的模式：只读，写入，追加等。所有可取值见如下的完全列表。这个参数是非强制的，默认文件访问模式为只读(r)。
buffering:如果buffering的值被设为0，就不会有寄存。如果buffering的值取1，访问文件时会寄存行。如果将buffering的值设为大于1的整数，表明了这就是的寄存区的缓冲大小。如果取负值，寄存区的缓冲大小则为系统默认。
不同模式打开文件的完全列表：

模式	描述
t	文本模式 (默认)。
x	写模式，新建一个文件，如果该文件已存在则会报错。
b	二进制模式。
+	打开一个文件进行更新(可读可写)。
U	通用换行模式（不推荐）。
r	以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
rb	以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。这是默认模式。一般用于非文本文件如图片等。
r+	打开一个文件用于读写。文件指针将会放在文件的开头。
rb+	以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。一般用于非文本文件如图片等。
w	打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
wb	以二进制格式打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。一般用于非文本文件如图片等。
w+	打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
wb+	以二进制格式打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。一般用于非文本文件如图片等。
a	打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
ab	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
a+	打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
ab+	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，创建新文件用于读写。

***********OS文件/目录方法**********
os.access(path, mode)


检验权限模式
2
os.chdir(path)


改变当前工作目录
3
os.chflags(path, flags)


设置路径的标记为数字标记。
4
os.chmod(path, mode)


更改权限
5
os.chown(path, uid, gid)


更改文件所有者
6
os.chroot(path)


改变当前进程的根目录
7
os.close(fd)


关闭文件描述符 fd
8
os.closerange(fd_low, fd_high)


关闭所有文件描述符，从 fd_low (包含) 到 fd_high (不包含), 错误会忽略
9
os.dup(fd)


复制文件描述符 fd
10
os.dup2(fd, fd2)


将一个文件描述符 fd 复制到另一个 fd2
11
os.fchdir(fd)


通过文件描述符改变当前工作目录
12
os.fchmod(fd, mode)


改变一个文件的访问权限，该文件由参数fd指定，参数mode是Unix下的文件访问权限。
13
os.fchown(fd, uid, gid)


修改一个文件的所有权，这个函数修改一个文件的用户ID和用户组ID，该文件由文件描述符fd指定。
14
os.fdatasync(fd)


强制将文件写入磁盘，该文件由文件描述符fd指定，但是不强制更新文件的状态信息。
15
os.fdopen(fd[, mode[, bufsize]])


通过文件描述符 fd 创建一个文件对象，并返回这个文件对象
16
os.fpathconf(fd, name)


返回一个打开的文件的系统配置信息。name为检索的系统配置的值，它也许是一个定义系统值的字符串，这些名字在很多标准中指定（POSIX.1, Unix 95, Unix 98, 和其它）。
17
os.fstat(fd)


返回文件描述符fd的状态，像stat()。
18
os.fstatvfs(fd)


返回包含文件描述符fd的文件的文件系统的信息，Python 3.3 相等于 statvfs()。
19
os.fsync(fd)


强制将文件描述符为fd的文件写入硬盘。
20
os.ftruncate(fd, length)


裁剪文件描述符fd对应的文件, 所以它最大不能超过文件大小。
21
os.getcwd()


返回当前工作目录
22
os.getcwdu()


返回一个当前工作目录的Unicode对象
23
os.isatty(fd)


如果文件描述符fd是打开的，同时与tty(-like)设备相连，则返回true, 否则False。
24
os.lchflags(path, flags)


设置路径的标记为数字标记，类似 chflags()，但是没有软链接
25
os.lchmod(path, mode)


修改连接文件权限
26
os.lchown(path, uid, gid)


更改文件所有者，类似 chown，但是不追踪链接。
27
os.link(src, dst)


创建硬链接，名为参数 dst，指向参数 src
28
os.listdir(path)


返回path指定的文件夹包含的文件或文件夹的名字的列表。
29
os.lseek(fd, pos, how)


设置文件描述符 fd当前位置为pos, how方式修改: SEEK_SET 或者 0 设置从文件开始的计算的pos; SEEK_CUR或者 1 则从当前位置计算; os.SEEK_END或者2则从文件尾部开始. 在unix，Windows中有效
30
os.lstat(path)


像stat(),但是没有软链接
31
os.major(device)


从原始的设备号中提取设备major号码 (使用stat中的st_dev或者st_rdev field)。
32
os.makedev(major, minor)


以major和minor设备号组成一个原始设备号
33
os.makedirs(path[, mode])


递归文件夹创建函数。像mkdir(), 但创建的所有intermediate-level文件夹需要包含子文件夹。
34
os.minor(device)


从原始的设备号中提取设备minor号码 (使用stat中的st_dev或者st_rdev field )。
35
os.mkdir(path[, mode])


以数字mode的mode创建一个名为path的文件夹.默认的 mode 是 0777 (八进制)。
36
os.mkfifo(path[, mode])


创建命名管道，mode 为数字，默认为 0666 (八进制)
37
os.mknod(filename[, mode=0600, device])
创建一个名为filename文件系统节点（文件，设备特别文件或者命名pipe）。

38
os.open(file, flags[, mode])


打开一个文件，并且设置需要的打开选项，mode参数是可选的
39
os.openpty()


打开一个新的伪终端对。返回 pty 和 tty的文件描述符。
40
os.pathconf(path, name)


返回相关文件的系统配置信息。
41
os.pipe()


创建一个管道. 返回一对文件描述符(r, w) 分别为读和写
42
os.popen(command[, mode[, bufsize]])


从一个 command 打开一个管道
43
os.read(fd, n)


从文件描述符 fd 中读取最多 n 个字节，返回包含读取字节的字符串，文件描述符 fd对应文件已达到结尾, 返回一个空字符串。
44
os.readlink(path)


返回软链接所指向的文件
45
os.remove(path)


删除路径为path的文件。如果path 是一个文件夹，将抛出OSError; 查看下面的rmdir()删除一个 directory。
46
os.removedirs(path)


递归删除目录。
47
os.rename(src, dst)


重命名文件或目录，从 src 到 dst
48
os.renames(old, new)


递归地对目录进行更名，也可以对文件进行更名。
49
os.rmdir(path)


删除path指定的空目录，如果目录非空，则抛出一个OSError异常。
50
os.stat(path)


获取path指定的路径的信息，功能等同于C API中的stat()系统调用。
51
os.stat_float_times([newvalue])
决定stat_result是否以float对象显示时间戳

52
os.statvfs(path)


获取指定路径的文件系统统计信息
53
os.symlink(src, dst)


创建一个软链接
54
os.tcgetpgrp(fd)


返回与终端fd（一个由os.open()返回的打开的文件描述符）关联的进程组
55
os.tcsetpgrp(fd, pg)


设置与终端fd（一个由os.open()返回的打开的文件描述符）关联的进程组为pg。
56
os.tempnam([dir[, prefix]])


Python3 中已删除。返回唯一的路径名用于创建临时文件。
57
os.tmpfile()


Python3 中已删除。返回一个打开的模式为(w+b)的文件对象 .这文件对象没有文件夹入口，没有文件描述符，将会自动删除。
58
os.tmpnam()


Python3 中已删除。为创建一个临时文件返回一个唯一的路径
59
os.ttyname(fd)


返回一个字符串，它表示与文件描述符fd 关联的终端设备。如果fd 没有与终端设备关联，则引发一个异常。
60
os.unlink(path)


删除文件路径
61
os.utime(path, times)


返回指定的path文件的访问和修改的时间。
62
os.walk(top[, topdown=True[, onerror=None[, followlinks=False]]])


输出在文件夹中的文件名通过在树中游走，向上或者向下。
63
os.write(fd, str)


写入字符串到文件描述符 fd中. 返回实际写入的字符串长度
64
os.path 模块


获取文件的属性信息。
65
os.pardir()


获取当前目录的父目录，以字符串形式显示目录名。
