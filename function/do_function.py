#! /usr/bin/env python3
def func1():
    print("Hello world")
def MAX(a,b):
    if a>b:
        return a
    else:
        return b
def change(x):
    print(id(x))
    x = 10
    print(id(x))
def changeme (mylist):
    mylist.append([1,2,3,4])
    print("function output:{}".format(mylist))
    return
def printinfo(arg1,*vartuple):
    print("output: ")
    print(arg1)
    for i in vartuple:
        print(i)

func1()
a = 1
print(id(a))
change(a)
print(a)

list = [10,20]
changeme(list)
print("main output:{}".format(list))

printinfo(10,20,30)

sum = lambda a,b : a+b
print(sum(10,20))
