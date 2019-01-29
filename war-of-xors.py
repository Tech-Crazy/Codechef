<<<<<<< HEAD
for _ in range(int(input())):
    count = 0
    n = int(input())
    arr = list(map(int,input().split()))
    i = 0
    j = 1
    while i < n:
        if j == n:
            i+=1
            j=i+1
        else:
            if (arr[i]^arr[j])%2==0:
                count+=1
            j+=1
    print(count)
=======
for _ in range(int(input())):
    count = 0
    n = int(input())
    arr = list(map(int,input().split()))
    i = 0
    j = 1
    while i < n:
        if j == n:
            i+=1
            j=i+1
        else:
            if (arr[i]^arr[j])%2==0:
                count+=1
            j+=1
    print(count)
>>>>>>> ef391bc2a214f90b5d6d707d9eb9bb54d3269d80
