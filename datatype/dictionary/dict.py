#! /usr/bin/env python3
# -*- coding:utf-8 -*-
from random import randint

dict = {'name':"shyhao",'age':22,'school':"ncepu"}

dict["class"] = "first" # update information
dict["age"] = 21

print("dict['age']:",dict["age"])
print("dict['class']:",dict["class"])

dict1 = {x:randint(60,100) for x in range(1,11)}
print(dict1)

d  = {k:v for k,v in dict1.items() if v>90}
print(d)