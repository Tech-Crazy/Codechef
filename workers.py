from collections import defaultdict
workers = defaultdict(list)
n = int(input())
cost = list(map(int,input().split()))
occu = list(map(int,input().split()))
for i in range(len(occu)):
    workers[occu[i]].append(cost[i])
for key in workers.keys():
    workers[key].sort()
mincoin = 0
if len(workers[1])==0 or len(workers[2])==0:
    mincoin = workers[3][0]
else:
    twoman=workers[1][0]+workers[2][0]
    if twoman<workers[3][0]:
        mincoin=twoman
    else:
        mincoin=workers[3][0]
print(mincoin)
