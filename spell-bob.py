<<<<<<< HEAD
T = int(input())
for _ in range(T):
    s = input()
    t = input()
    cond = False
    for i in range(3):
        if s[i] == 'o' or t[i] == 'o':
            cnt = 0
            for j in range(3):
                if j != i:
                    if s[j] == 'b' or t[j] == 'b':
                        cnt += 1
            if cnt == 2:
                cond = True
    print("yes" if ok else "no"); 
=======
T = int(input())
for _ in range(T):
    s = input()
    t = input()
    cond = False
    for i in range(3):
        if s[i] == 'o' or t[i] == 'o':
            cnt = 0
            for j in range(3):
                if j != i:
                    if s[j] == 'b' or t[j] == 'b':
                        cnt += 1
            if cnt == 2:
                cond = True
    print("yes" if ok else "no"); 
>>>>>>> ef391bc2a214f90b5d6d707d9eb9bb54d3269d80
