import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())

    nums = [int(num) for num in input().split()]

    res = 0

    maxNum = nums[0]

    i = 0

    while i < len(nums):

        while i+1 < len(nums) and  nums[i] * nums[i+1] > 0:
            maxNum = max(maxNum, nums[i+1])
            i += 1

        res += maxNum
        
        i += 1

        if i < len(nums):
            maxNum = nums[i]
       
    print(res)








