for _ in range(int(input())):
	n = int(input())
	s = list(map(int,input().split()))
	i = 0
	j = 1
	mindiff = 10000000000000000000000000000
	while i<=n-2:
		if j == n:
			i += 1
			j = i+1
		else:
			if abs(s[i]-s[j])<mindiff:
				mindiff = abs(s[i]-s[j])
			j+=1
	print(mindiff)