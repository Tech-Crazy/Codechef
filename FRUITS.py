for _ in range(int(input())):
    a, o, c = map(int, input().split())
    diff = abs(a - o)
    if c >= diff:
        print(0)
    else:
        print(abs(c - diff))