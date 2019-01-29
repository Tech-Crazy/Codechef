<<<<<<< HEAD
for _ in range(int(input())):
    n,x,s = map(int,input().split())
    swaps = [0]*n
    swaps[x-1] = 1
    for _ in range(s):
        a,b = map(int,input().split())
        swaps[a-1],swaps[b-1] = swaps[b-1],swaps[a-1]
    print(swaps.index(1)+1)
=======
for _ in range(int(input())):
    n,x,s = map(int,input().split())
    swaps = [0]*n
    swaps[x-1] = 1
    for _ in range(s):
        a,b = map(int,input().split())
        swaps[a-1],swaps[b-1] = swaps[b-1],swaps[a-1]
    print(swaps.index(1)+1)
>>>>>>> ef391bc2a214f90b5d6d707d9eb9bb54d3269d80
