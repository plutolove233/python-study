#! /usr/bin/env python3
print("test1")
basket = {'apple','banana','apple','pear'}
print(basket)   # 显示去重功能
print('apple' in basket)
print("test2")
a = {1,2,3,4,5,6,7,8,9}
b = {2,4,6,8}
print(f"{a-b=}")
print(f"{a|b=}")
print(f"{a&b=}")
print(f"{a^b=}")
print("test3")
thisset = set(("Google","Runnoob","Taobao"))
thisset.update({1,2})
print(thisset)
thisset.discard("Google")
print(thisset)