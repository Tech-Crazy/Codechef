from itertools import combinations

def subsets(notes):
    sets = []
    for i in range(1,len(notes)+1):
        sets.extend(combinations(notes,i))
    return sets

for _ in range(int(input())):
    ans = "No"
    n,m = map(int,input().split())
    notes = []
    for _ in range(n):
        notes.append(int(input()))
    
    sets = subsets(notes)

    for s in sets:
        if m == sum(s):
            ans = "Yes"
            break

    print(ans)