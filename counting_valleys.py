def countingValleys(steps, path):
    # Write your code here
    count = temp = num_0f_valleys = 0
    for x in path:
        if x is 'U':
            count += 1
        elif x is 'D':
            count -= 1
        if count < 0 and temp != -1:
            temp = -1
        if count == 0 and temp == -1:
            temp = 0
            num_0f_valleys += 1
    return num_0f_valleys  
