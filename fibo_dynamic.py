def fib(n):
	alist=[]
	if n<0:
		return False
	if n==0 or n==1:
		return n
	else:
		alist.append(fib(n-1)+fib(n-2))
		return alist

fib(5)