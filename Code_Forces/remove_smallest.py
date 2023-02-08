t = int(input())

for _ in range(t):
    n = int(input())
    arr = [int(num) for num in input().split()]

    arr.sort()
    ans = "YES"

    for i in range(n-1):
        if arr[i+1] - arr[i] > 1:
            ans = "NO"
            break

    print(ans)
    

