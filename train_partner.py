arr = ['LB','MB','UB','LB','MB','UB','SL','SU']
for _ in range(int(input())):
	seat = int(input())
	if seat%7 == 0:
		print("{0}{1}".format(seat+1,arr[(seat+1)%8-1]))
	elif seat%8 == 0:
		print("{0}{1}".format(seat-1,arr[(seat-1)%8-1]))
	elif seat%8 <= 3:
		print("{0}{1}".format(seat+3,arr[(seat+3)%8-1]))
	elif seat%8>=4 and seat%8<7:
		print("{0}{1}".format(seat-3,arr[(seat-3)%8-1]))