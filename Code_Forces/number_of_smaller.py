n, m = [int(num) for num in input().split()]

arr1 = [int(num) for num in input().split()]
arr2 = [int(num) for num in input().split()]

res = [0] * m 

i = 0

for j in range(len(arr2)):
    while i < n and arr1[i] < arr2[j]:
        i += 1

    res[j] = i

print(*res)




    
    
