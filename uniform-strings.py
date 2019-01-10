for _ in range(int(input())):
    s = input()
    count = 0
    for i in range(1,len(s)+1):
        if s[i%8] != s[(i-1)%8]:
            count+=1
    if count<=2:
        print('uniform')
    else:
        print('non-uniform')
