for _ in range(int(input())):
	num = int(input())
	total = 0
	while num>0:
		total+=num%10
		num=int(num/10)
	print(total)