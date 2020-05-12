#coding=utf-8

#list.extend(L)	通过添加指定列表的所有元素来扩充列表，相当于 a[len(a):] = L。

array1 = [1,2,3,4]
array2 = [5,6,7,8]
array1.extend(array2)    #extend 相当 + 号
array1 = array1+ array2
print("array1: ", array1)


#堆栈 （ 后进先出 ）pop
stack = [3, 4, 5]
stack.append(6)
stack.append(7)
stack.pop()
print stack  # >>>stack  [3,4,5,6]

#队列 （ 先进先出 ）popleft

from collections import deque
queue = deque(['linn', 'john', 'lisa'])
queue.append("Dav")
queue.append("lucy")

left = queue.popleft()
print "left: ", left

print "queue: ", queue
