for _ in range(int(input())):
	n,m = map(int,input().split())
	jobs = list(range(1,n+1))
	done = list(map(int,input().split()))
	for d in done:
		jobs.remove(d)
	chef = [jobs[j] for j in range(0,len(jobs),2)]
	ast = [jobs[j] for j in range(1,len(jobs),2)]
	print(" ".join(map(str,chef)))
	print(" ".join(map(str,ast)))