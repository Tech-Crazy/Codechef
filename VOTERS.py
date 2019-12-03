n1, n2, n3 = map(int, input().split())
voters1 = []
common = set()
for _ in range(n1):
    voters1.append(int(input()))
for _ in range(n2):
    el = int(input())
    if el in voters1:
        common.add(str(el))
for _ in range(n3):
    el = int(input())
    if el in voters1:
        common.add(str(el))
print(len(common))
print(" ".join(sorted(list(common))))