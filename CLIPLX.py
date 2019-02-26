for _ in range(int(input())):
    x,y = map(int,input().split())
    wins = 0
    while x > 0:
        if x > 2*y:
            x -= 2
            wins += 1
            y -= 1
        else:
            x -= 1
            y -= 1
    print(wins)