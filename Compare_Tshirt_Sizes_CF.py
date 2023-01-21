import sys
input = sys.stdin.readline
 
t = int(input())
 
for _ in range(t):
 
    s1, s2 = input().split()
 
    if s1[-1] == "S":
 
        if s2[-1] == "S":
            if len(s1) > len(s2):
                print("<")
            elif len(s1) < len(s2):
                print(">")
            else:
                print("=")
        
        else:
            print("<")
 
    elif s1[-1] == "M":
 
        if s2[-1] == "S":
            print(">")
        elif s2[-1] == "M":
            print("=")
        else:
            print("<")
 
    else:
 
        if s2[-1] == "L":
            if len(s1) > len(s2):
                print(">")
            elif len(s1) < len(s2):
                print("<")
            else:
                print("=")
 
        else:
            print(">")
