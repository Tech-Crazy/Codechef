from itertools import combinations
arr = []
for _ in range(int(input())):
    arr.append(int(input()))
combs = combinations(arr,2)
print(len([el for el in combs if sum(el) == 0]))