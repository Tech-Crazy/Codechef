<<<<<<< HEAD
for _ in range(int(input())):
    n,k = list(map(int,input().split()))
    glist = list(map(int,input().split()))
    maxg = 0
    for i in range(0,n-k+1):
        gsum = 0
        for g in glist[i:i+k]:
            gsum+=g
        if gsum>maxg:
            maxg = gsum
    print(maxg)
=======
for _ in range(int(input())):
    n,k = list(map(int,input().split()))
    glist = list(map(int,input().split()))
    maxg = 0
    for i in range(0,n-k+1):
        gsum = 0
        for g in glist[i:i+k]:
            gsum+=g
        if gsum>maxg:
            maxg = gsum
    print(maxg)
>>>>>>> ef391bc2a214f90b5d6d707d9eb9bb54d3269d80
