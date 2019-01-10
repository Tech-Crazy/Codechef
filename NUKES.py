a,n,k = map(int,input().split())
reactors = [0]*k
for i in range(k):
    reactors[i] = a%(n+1)
    a = a//(n+1)
print(' '.join(list(map(str,reactors))))