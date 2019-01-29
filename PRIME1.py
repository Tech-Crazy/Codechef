from math import sqrt

def isPrime(n):
    i=3
    if n == 1:
        return False
    while i<=sqrt(n):
        if n%i == 0:
            return False
        i+=1
    return True

for _ in range(int(input())):
    m,n = map(int,input().split())
    lst = [el for el in range(m,n+1) if el%2!=0]
    print('\n'.join(map(str,filter(isPrime,lst))))