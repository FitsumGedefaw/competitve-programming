t = int(input())

for _ in range(t):
    ans = 'YES'
    
    n = int(input())
    
    nums = [int(num) for num in input().split()]
    
    s = input()

    d = {}
    
    for i in range(n):
        if nums[i] not in d:
            d[nums[i]] = s[i]
            
        elif d[nums[i]] != s[i]:
            ans= 'NO'
            break
        
    print(ans)
