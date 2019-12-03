while True:
    n = int(input())
    if n == 0:
        break
    perm = list(map(int,input().split()))
    new_perm = []
    for el in sorted(perm):
        new_perm.append(perm.index(el)+1)
    if perm == new_perm:
        print('ambiguous')
    else:
        print('not ambiguous')