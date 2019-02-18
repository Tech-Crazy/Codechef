from math import gcd
for _ in range(int(input())):
    n,a,b,k = map(int,input().split())
    appy = n//a
    chef = n//b
    lcm = (a*b)/gcd(a,b)
    neither = n//lcm
    solve = appy+chef-2*neither
    if solve>=k:
        print("Win")
    else:
        print("Lose")