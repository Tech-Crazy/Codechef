for _ in range(int(input())):
    x, y, k, n = map(int, input().split())
    isOk = False
    while n > 0:
        p, c = map(int, input().split())
        if c <= k and p + y >= x:
            isOk = True
        n -= 1
    if isOk:
        print("LuckyChef")
    else:
        print("UnluckyChef")