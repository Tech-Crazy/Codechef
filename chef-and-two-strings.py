for _ in range(int(input())):
    s1 = input()
    s2 = input()
    mincount=0
    maxcount=0
    for i in range(len(s1)):
        if s1[i] == '?' or s2[i] == '?':
            maxcount+=1
        elif s1[i] != s2[i]:
            mincount+=1
            maxcount+=1
    print(mincount,maxcount)
