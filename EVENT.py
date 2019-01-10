days = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
for _ in range(int(input())):
	day1,day2,l,r = input().split()
	num = days.index(day2)-days.index(day1)+1
	l,r = int(l),int(r)
	if num==l or num==r:
		print(num)
	elif num>l and num<r:
		print("many")
	elif num<l or num>r:
		print("impossible")