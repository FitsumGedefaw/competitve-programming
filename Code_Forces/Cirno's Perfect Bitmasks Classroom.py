t = int(input())

for _ in range(t):
    x = int(input())
    x = bin(x)

    idxOfFirstOne = -1
    for i in range(len(x)-1, 1, -1):
        if x[i] == "1":
            idxOfFirstOne = i
            break
    
    y = ["0"] * (len(x)-1 - idxOfFirstOne)
    y.insert(0, "1")

    F = 0
    for i in range(idxOfFirstOne - 1, -1, -1):
        if x[i] == "1":
            F = 1

    if F == 1:
        y = "".join(y)
        print(int(y, 2))
    else:
        for i in range(len(y)-1, -1, -1):
            if i == 0:
                y = "1" + "".join(y)
            
            elif y[i] == "0":
                y[i] = "1"
                y = "".join(y)
                break

        print(int(y, 2))
