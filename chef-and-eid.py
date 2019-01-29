<<<<<<< HEAD
from itertools import combinations

def diff(elem):
    return abs(elem[0]-elem[1])

for _ in range(int(input())):
    n = int(input())
    combos = list(combinations(list(map(int,input().split())),2))
    combos.sort(key=diff)
    print(diff(combos[0]))
=======
from itertools import combinations

def diff(elem):
    return abs(elem[0]-elem[1])

for _ in range(int(input())):
    n = int(input())
    combos = list(combinations(list(map(int,input().split())),2))
    combos.sort(key=diff)
    print(diff(combos[0]))
>>>>>>> ef391bc2a214f90b5d6d707d9eb9bb54d3269d80
