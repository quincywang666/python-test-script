#!/usr/local/bin/python3.7

list=[1,2,3,4]
it=iter(list)
for x in it:
	print (x,end="  ")


import sys
list=[1,2,3,4]
it=iter(list)
while True:
	try:
		print(next(it))
	except StopIteration:
		sys.exit()

