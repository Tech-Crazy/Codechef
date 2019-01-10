for _ in range(int(input())):
    n,u,d = map(int,input().split())
    hills = list(map(int,input().split()))
    p = 1
    bcount = 0
    for i in range(1,n):
        if hills[i]>hills[i-1]+u:
            bcount = 1
            break
        elif hills[i]<hills[i-1]-d:
            if p==1:
                p-=1
                continue
            else:
                bcount = 1
                break
    if bcount == 0:
        print(i+1)
    else:
        print(i)
