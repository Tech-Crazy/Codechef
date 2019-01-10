for _ in range(int(input())):
	n = int(input())
	div = 5
	zeros = 0
	while n/div>=1:
		zeros+=int(n/div)
		div*=5
	print(zeros)