from math import gcd

for _ in range(int(input())):
    arr = list(map(int,input().split()))
    arr = arr[1:]
    hcf = arr[0]
    for i in range(1,len(arr)):
        hcf = gcd(hcf,arr[i])
    arr = [str(el//hcf) for el in arr]
    print(" ".join(arr))