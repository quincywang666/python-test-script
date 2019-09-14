for n in range(2,3):
	for x in range(2,n):
		if n % x == 0:
			print(n,'equals',x,'*',n//x)
			break
	else:
		print(n,'is a prime number')
