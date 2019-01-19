def josephus(n,k):
    circle = list(range(1,n+1))
    return josephrec(n-1,k-1,circle)

def josephrec(n,k,rec):
    if len(rec)==1:
        return rec[0]
    else:
        i = k%n
        return josephrec(n-1,k,rec[i+1:]+rec[:i])

for _ in range(int(input())):
    n,k = map(int,input().split())
    print(josephus(n,k))