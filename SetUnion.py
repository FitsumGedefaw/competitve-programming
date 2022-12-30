# Enter your code here. Read input from STDIN. Print output to STDOUT
# Enter your code here. Read input from STDIN. Print output to STDOUT
numOfEnglishSubscribers = int(input())
englishSubscribers = input().split()
numOfFrenchSubscribers = int(input())
frenchSubscribers = set(input().split())

numOfEandFSubscribers = 0

for student in englishSubscribers:
    if student in frenchSubscribers:
        numOfEandFSubscribers += 1

answer = len(englishSubscribers) + len(frenchSubscribers) - numOfEandFSubscribers
print(answer)
