#coding=utf-8
import sys

try:
    f = open('myfile.txt')
    print("f:", f)
    s = f.readline()
    print("s: ", s)
    print "i:", s.strip('f')
    i = int(s.strip("f"))
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise
else:
    print "no exception!"
finally:
    print "有没有异常，最后都会走我。"
    
