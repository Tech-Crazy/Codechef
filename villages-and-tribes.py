<<<<<<< HEAD
for _ in range(int(input())):
    area = input().strip('.')
    acount=area.count('A')
    bcount=area.count('B')
    for terr in area.split('A'):
        if '.' in terr and 'B' not in terr:
            acount+=len(terr)
    for terr in area.split('B'):
        if '.' in terr and 'A' not in terr:
            bcount+=len(terr)
    print(acount,bcount)
=======
for _ in range(int(input())):
    area = input().strip('.')
    acount=area.count('A')
    bcount=area.count('B')
    for terr in area.split('A'):
        if '.' in terr and 'B' not in terr:
            acount+=len(terr)
    for terr in area.split('B'):
        if '.' in terr and 'A' not in terr:
            bcount+=len(terr)
    print(acount,bcount)
>>>>>>> ef391bc2a214f90b5d6d707d9eb9bb54d3269d80
