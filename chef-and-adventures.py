<<<<<<< HEAD
for _ in range(int(input())):
    n,m,x,y = map(int,input().split())
    n-=1
    m-=1
    if n%x!=0 or m%y!=0:
        if ((n-1)%x==0 and (m-1)%y==0) and (n-1!=-1 and m-1!=-1):
            print('Chefirnemo')
        else:
            print('Pofik')
    elif n%x==0 and m%y==0:
        print('Chefirnemo')
=======
for _ in range(int(input())):
    n,m,x,y = map(int,input().split())
    n-=1
    m-=1
    if n%x!=0 or m%y!=0:
        if ((n-1)%x==0 and (m-1)%y==0) and (n-1!=-1 and m-1!=-1):
            print('Chefirnemo')
        else:
            print('Pofik')
    elif n%x==0 and m%y==0:
        print('Chefirnemo')
>>>>>>> ef391bc2a214f90b5d6d707d9eb9bb54d3269d80
