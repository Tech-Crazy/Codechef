import random
a,b = map(int,input().split())
digs = [1,2,3,4,5,6,7,8,9]
ans = a-b
digits = list(str(ans))
index = random.randint(0,len(digits)-1)
randig = digits[index]
digs.remove(int(randig))
digits[index] = str(*random.sample(digs,1))
print(''.join(digits))