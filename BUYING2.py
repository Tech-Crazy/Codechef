for _ in range(int(input())):
    n,k = map(int,input().split())
    notes = list(map(int,input().split()))
    count = 0
    if not all((el-k>0 for el in notes)):
        print(-1)
        continue
    i = 0
    while i<len(notes):
        notes[i]-=k
        count+=1
        if notes[i]<k:
            i+=1
    print(count)