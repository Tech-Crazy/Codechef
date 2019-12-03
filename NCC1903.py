for _ in range(int(input())):
    n = int(input())
    k = int(input())
    arr = list(sorted(map(int,input().split())))
    count = 0
    for el in arr:
        n -= el
        if n<0:
            break
        count+=1
    print(count)