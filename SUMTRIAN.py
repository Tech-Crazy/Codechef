for _ in range(int(input())):
    n = int(input())
    i = 0
    maxsum = 0
    while n > 0:
        nums = list(map(int,input().split()))
        if len(nums) == 1:
            maxsum += nums[0]
        else:
            if nums[i] < nums[i+1]:
                maxsum += nums[i+1]
                i += 1
            else:
                maxsum += nums[i]
        n -= 1
    print(maxsum)