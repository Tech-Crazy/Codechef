days = [1,1,1,1,1,1,0]
for _ in range(int(input())):
    n,k,s = list(map(int,input().split()))
    if n<k:
        ans = -1
    else:
        if n*6 >= k*7:
            ans = (k*s)/n
            if (k*s)%n>0:
                ans+=1
        elif n == k and s<7:
            ans = s
        else:
            ans = -1
    print(int(ans))
