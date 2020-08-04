#coding=utf-8
# os.chdir(path) 方法用于改变当前工作目录到指定的路径 path 指定新路径
#返回值
# 如果允许访问返回 True , 否则返回False

import os, sys
path = '/Users/brilljoy/Space/myGit/python_study/day8'

#查看当前工作目录
retval = os.getcwd()
print "当前工作目录为%s"%retval

#修改当前工作目录
os.chdir(path)

#查看修改后的工作目录
retval = os.getcwd()

print "目录修改成功 %s" %retval
