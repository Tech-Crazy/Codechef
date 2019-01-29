<<<<<<< HEAD
for _ in range(int(input())):
    sides = list(map(int,input().split()))
    flag = 0
    if len(set(sides))==2:
        for elem in set(sides):
            if sides.count(elem)!=2:
                flag = 1
    else:
        flag = 1
    if flag==0:
        print('YES')
    else:
        print('NO')
=======
for _ in range(int(input())):
    sides = list(map(int,input().split()))
    flag = 0
    if len(set(sides))==2:
        for elem in set(sides):
            if sides.count(elem)!=2:
                flag = 1
    else:
        flag = 1
    if flag==0:
        print('YES')
    else:
        print('NO')
>>>>>>> ef391bc2a214f90b5d6d707d9eb9bb54d3269d80
