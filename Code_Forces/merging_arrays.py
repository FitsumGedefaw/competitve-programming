n, m = [int(num) for num in input().split()]

arr1 = [int(num) for num in input().split()]
arr2 = [int(num) for num in input().split()]

res = []

i = j = 0

while i < len(arr1) and j < len(arr2):
    if arr1[i] <= arr2[j]:
        res.append(arr1[i])
        i += 1

    else:
        res.append(arr2[j])
        j += 1

    
while i < len(arr1):
    res.append(arr1[i])
    i += 1

while j < len(arr2):
    res.append(arr2[j])
    j += 1

print(*res)



