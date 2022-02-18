#! /usr/bin/python3

# while True:
#     try:
#         x = int(input("please input one number:"))
#         break
#     except ValueError:
#         print("你输入的不是数字")
import sys

class MyError(Exception):
    def __init__(self,value):
        self.value = value
    def __str__(self):
        return repr(self.value)

for arg in sys.argv:
    try:
        f = open(arg,'r')
    except IOError:#发生异常时执行
        print("can't open",arg)
    else: #没有异常时执行
        print(arg,'has',len(f.readlines()),'lines')
        f.close()
    finally:
        print("无论是否异常都会执行")
try:
    raise MyError(2*2)
except MyError as e:
    print("My exception occurred,value:",e.value)