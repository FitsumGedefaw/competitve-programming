n, k = [int(num) for num in input().split()]

arr = [int(num) for num in input().split()]

arr.sort()

if k == n:
    print(arr[k-1])

elif k > 0 and arr[k-1] != arr[k]:
     print(arr[k-1])

elif k == 0:
    if arr[0] > 1:
        print(1)
    else:
        print(-1)
        
else:
    print(-1)

