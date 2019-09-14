#!/usr/local/bin/python3.7

num=int(input("输入一个数字："))
if num%2==0:
	if num%3==0:
		print ("你输入的数字可以整除2 和 3")
	else:
		print ("你输入的数字可以整除2，但不能整除3")
else:
	if num%3==0:
		print ("你输入的数字可以整除 3，但不能整除2")
	else:
		print ("你输入的数字不能整除2 和 3")


