# Enter your code here. Read input from STDIN. Print output to STDOUT
numOfEnglishSubscribers = input()
englishSubscribers = list(map(int, input().split()))
numOfFrenchSubscribers = input()
frenchSubscribers = list(map(int, input().split()))

onlyEnglishSubscribers = [student for student in englishSubscribers if student not in frenchSubscribers]

print(len(onlyEnglishSubscribers))

