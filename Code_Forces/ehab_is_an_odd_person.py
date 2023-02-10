n = int(input())

arr = [int(num) for num in input().split()]

even = 0
odd = 0

for num in arr:
    if num%2 == 0:
        even = 1

    else:
        odd = 1

if odd and even:
    print(*sorted(arr))

else:
    print(*arr)
