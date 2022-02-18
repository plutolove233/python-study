#! /usr/bin/env python3
# -*- coding:utf-8 -*-
import os
from random import randint

os.system("clear")
list = [randint(1,100) for _ in range(1,10)]
print(list[0:-1])

list.append(2.46)#  update data
print("添加后的数据：",list)

list.insert(2,12)
print("insert后的数据：",list)

del list[1]
print("删除后的数据：",list)
list.pop()
print("pop后的数据：",list)