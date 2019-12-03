for _ in range(int(input())):
    n = input()
    if n.endswith('5'):
        print(1)
    elif n.endswith('0'):
        print(0)
    else:
        print(-1)