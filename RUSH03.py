from itertools import combinations
n,k,s = map(int,input().split())
gangsters = []
for _ in range(n):
    gangsters.append(int(input()))
combs = combinations(gangsters,k)
for el in combs:
    if sum(el) == s:
        print("\n".join(str(e) for e in sorted(el)))