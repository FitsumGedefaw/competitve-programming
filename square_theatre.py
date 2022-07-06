from math import ceil
n,m,a=map(int,input().split()) 
f1 = ceil(n/a)
f2 = ceil(m/a)
print(f1 * f2)
