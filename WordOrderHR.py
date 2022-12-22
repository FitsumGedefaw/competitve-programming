# Enter your code here. Read input from STDIN. Print output to STDOUT
words = []
numOfWords = int(input())

for i in range(numOfWords):
    val = input()
    words.append(val)
    
d = {}

for w in words:
    d[w] = d.get(w, 0) + 1

temp = ""

for w in d:
    temp += str(d[w])
    
print(len(d))
print(temp)

    
    
    
    
