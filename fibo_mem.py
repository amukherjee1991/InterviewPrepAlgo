mem={}
def fibo(n):
	if n==0:
		return 0
	if n==1:
			return 1
	elif n>1:
		if n not in mem:
			mem[n]=fibo(n-1)+fibo(n-2)
		return mem[n]
	return -1

# print fibo(100)


def fibo_rec(n):
	if n==0:
		return 0
	if n==1:
		return 1
	if n>1:
		return fibo_rec(n-1)+fibo(n-2)

print fibo_rec(1000)
# del mem
print mem