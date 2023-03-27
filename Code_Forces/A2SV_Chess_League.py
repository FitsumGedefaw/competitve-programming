
def findWinnerHelper(arr, left, right):
    if left == right:
        return [[arr[left], left]]
    
    mid = (left+right)//2
    leftWinners = findWinnerHelper(arr,left, mid)
    #print(leftWinners, "left: ", left, "right: ", right)
    rightWinners = findWinnerHelper(arr, mid+1, right)

    leftWinners.sort()
    rightWinners.sort()
    res = []

    for rating, idx in leftWinners:
        weakestOpponentRating = rightWinners[0][0]
        if rating > weakestOpponentRating or (weakestOpponentRating - rating <= k):
            res.append([rating, idx])

    for rating, idx in rightWinners:
        weakestOpponentRating = leftWinners[0][0]
        if rating > weakestOpponentRating or (weakestOpponentRating - rating <= k):
            res.append([rating, idx])
    
    return res


n, k = [int(num) for num in input().split()]
players = [int(num) for num in input().split()]

possibleWinners = findWinnerHelper(players, 0, len(players)-1)
possibleWinnerIndices = [winner[1]+1 for winner in possibleWinners]
possibleWinnerIndices.sort()

print(*possibleWinnerIndices)





