from itertools import combinations
for _ in range(int(input())):
	n = int(input())
	s = list(combinations(map(int,input().split()),2))
	mindiff = abs(s[0][0]-s[0][1])
	for temp in s:
		if abs(temp[0]-temp[1])<mindiff:
			mindiff = abs(temp[0]-temp[1])
	print(mindiff)