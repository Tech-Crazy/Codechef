<<<<<<< HEAD
def upandlow(string):
    lcount=0
    ucount=0
    for c in string:
        if c.isupper():
            ucount+=1
        elif c.islower():
            lcount+=1
    return (lcount,ucount)
            
for _ in range(int(input())):
    n,k = map(int,input().split())
    l,u = upandlow(input())
    if l>k and u<=k:
        print('chef')
    elif u>k and l<=k:
        print('brother')
    elif l<=k and u<=k:
        print('both')
    elif l>k and u>k:
        print('none')
    
=======
def upandlow(string):
    lcount=0
    ucount=0
    for c in string:
        if c.isupper():
            ucount+=1
        elif c.islower():
            lcount+=1
    return (lcount,ucount)
            
for _ in range(int(input())):
    n,k = map(int,input().split())
    l,u = upandlow(input())
    if l>k and u<=k:
        print('chef')
    elif u>k and l<=k:
        print('brother')
    elif l<=k and u<=k:
        print('both')
    elif l>k and u>k:
        print('none')
    
>>>>>>> ef391bc2a214f90b5d6d707d9eb9bb54d3269d80
