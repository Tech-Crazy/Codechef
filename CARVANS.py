for _ in range(int(input())):
    n = int(input())
    cars = list(map(int,input().split()))
    count = 1
    topcar = cars[0]
    for i in range(1,n):
        if topcar > cars[i]:
            count += 1
        else:
            cars[i] = topcar
        topcar = cars[i]
    print(count)