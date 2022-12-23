# Enter your code here. Read input from STDIN. Print output to STDOU
n, m = list(map(int, input().split()))
arr = input().split()
A = set(input().split())
B = set(input().split())

happ = 0

for char in arr:
    if char in A:
        happ += 1
        
    elif char in B:
        happ -= 1
        
print(happ)


        


