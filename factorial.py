for _ in range(int(input())):
	fact_list = [1,]
	n = int(input())
	while n>1:
		fact_list.append(n*fact_list[-1])
		n-=1
	print(fact_list.pop())