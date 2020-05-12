#coding=utf-8
import sys

def fibonacci(n):
    a,b,counter = 0, 1, 0
    while True:
        if(counter > n):
            return
        yield a
        a, b = b, a+b
        print("a: ", a)
        counter += 1

f = fibonacci(10)

while True:
    try:
        print(next(f))
    except StopIteration:
        sys.exit()
