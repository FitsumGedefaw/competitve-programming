t = int(input())

for _ in range(t):
    numOfProgrammers, numOfMathematicians = [int(num) for num in input().split()]
    print(min(numOfProgrammers, numOfMathematicians, (numOfProgrammers + numOfMathematicians)//4))
    
