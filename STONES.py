for _ in range(int(input())):
    jewels = set(input())
    stones = list(input())
    count = 0
    for r in jewels:
        count+=stones.count(r)
    print(count)