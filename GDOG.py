for _ in range(int(input())):
    n, k = map(int, input().split())
    print(max([n%i for i in range(2, k+1)]))