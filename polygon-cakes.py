<<<<<<< HEAD
from math import gcd
for _ in range(int(input())):
    n,a,k = list(map(int,input().split()))
    S = 180*(n-2)
    x = a*n*(n-1)+(k-1)*(2*S-2*a*n)
    y = n*(n-1)
    tmp = gcd(x,y)
    x=x/tmp
    y=y/tmp
    print(int(x),int(y))
=======
from math import gcd
for _ in range(int(input())):
    n,a,k = list(map(int,input().split()))
    S = 180*(n-2)
    x = a*n*(n-1)+(k-1)*(2*S-2*a*n)
    y = n*(n-1)
    tmp = gcd(x,y)
    x=x/tmp
    y=y/tmp
    print(int(x),int(y))
>>>>>>> ef391bc2a214f90b5d6d707d9eb9bb54d3269d80
