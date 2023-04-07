n = int(input())

for source in range(n):
    row = [int(num) for num in input().split()]
    destinations = [idx+1 for idx, val in enumerate(row) if val == 1]

    print(len(destinations), *destinations)
