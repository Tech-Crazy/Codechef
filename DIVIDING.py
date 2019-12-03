n = int(input())
arr = list(map(int, input().split()))
if n*(n+1)/2 == sum(arr):
    print("YES")
else:
    print("NO")