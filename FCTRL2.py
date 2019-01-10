def fact(n):
	prod = 1
	while n>1:
		prod*=n
		n-=1
	return prod
for _ in range(int(input())):
	n = int(input())
	print(fact(n))