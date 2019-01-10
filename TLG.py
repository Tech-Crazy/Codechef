n = int(input())
leader = -1
lead = -1
stot = 0
ttot = 0
for _ in range(n):
	s,t = map(int,input().split())
	stot+=s
	ttot+=t
	diff = stot-ttot
	if diff>0 and abs(diff)>lead:
		leader = 1
		lead = abs(diff)
	elif diff<0 and abs(diff)>lead:
		leader = 2
		lead = abs(diff)
print(leader,lead)