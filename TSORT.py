l = []
for _ in range(int(input())):
	l.append(int(input()))
l.sort()
print('\n'.join(map(str,l)))