# /user/bin/env python
#  -*- coding:utf-8 -*-
# Author:CLL
age = 50
comon=0
for i in range(10):
    if comon<3:
        userage = int(input("请输入你的年龄："))
        if userage == age:
            print("正确")
        elif userage>age:
            print("大了")
        else:
            print("小了")
    else:
        con = input("你想继续吗")
        if con == "y":
            comon=0
            continue
        else:
            print("bye")
            break
    comon+=1

