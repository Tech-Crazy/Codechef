for _ in range(int(input())):
    g = int(input())
    for _ in range(g):
        i,n,q = map(int,input().split())
        if i == 1:
            if q == 1:
                ans = n//2
            else:
                ans = n-n//2
        elif i == 2:
            if q == 1:
                ans = n-n//2
            else:
                ans = n//2
        print(ans)