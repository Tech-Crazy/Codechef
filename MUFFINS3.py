def maxrem(n):
	div = 2
	maxdiv = 0
	maxcup = 0
	if n == 2:
		return 2
	while div<=n//2+1:
		if n%div > maxcup:
			maxdiv = div
			maxcup = n%div
		div+=1
	return maxdiv
for _ in range(int(input())):
	n = int(input())
	print(maxrem(n))