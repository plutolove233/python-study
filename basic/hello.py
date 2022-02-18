#! /usr/bin/env python3
# -*- coding:utf-8 -*-
person = 'shy hao'
ticket = 43.9
message = '''name = %s
price = %f
'''%(person,ticket)
print(message)
print("name = %s\nprice = %.2f"%(person,ticket))

age = 18
name = "plutolove"
print(f"you're {age} old,you're name is {name}")
print("you're {} old,you're name is {}".format(age,name),end='12')
