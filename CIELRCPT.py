for _ in range(int(input())):
	minus = 2048
	n = int(input())
	count=0
	while n!=0:
		if n<minus:
			minus/=2
		elif n>=minus:
			n-=minus
			count+=1
	print(count)