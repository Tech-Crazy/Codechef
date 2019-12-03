def maxSum(triangle):
    if len(triangle) == 1:
        return max(triangle[0])
    else:
        for i in range(len(triangle[0])):
            print(triangle)
            return max(triangle[0][i]+maxSum(triangle[1:]))

for _ in range(int(input())):
    n = int(input())
    triangle = []
    for i in range(n):
        triangle.append(list(map(int, input().split())))
    print(triangle)
    maxsum = maxSum(triangle)
    print(maxsum)