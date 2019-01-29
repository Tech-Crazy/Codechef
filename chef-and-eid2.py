<<<<<<< HEAD
for _ in range(int(input())):
    n = int(input())
    combos = list(map(int,input().split()))
    combos.sort()
    mindiff = abs(combos[0]-combos[1])
    for i in range(1,len(combos)-1):
        if abs(combos[i]-combos[i+1])<mindiff:
            mindiff = abs(combos[i]-combos[i+1])
    print(mindiff)
=======
for _ in range(int(input())):
    n = int(input())
    combos = list(map(int,input().split()))
    combos.sort()
    mindiff = abs(combos[0]-combos[1])
    for i in range(1,len(combos)-1):
        if abs(combos[i]-combos[i+1])<mindiff:
            mindiff = abs(combos[i]-combos[i+1])
    print(mindiff)
>>>>>>> ef391bc2a214f90b5d6d707d9eb9bb54d3269d80
