for _ in range(int(input())):
    n = int(input())
    total = sum(list(map(int,input().split())))
    if total%2 == 0:
        print('NO')
    else:
        print('YES')
