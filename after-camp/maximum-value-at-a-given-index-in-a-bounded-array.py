class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        def check(val):
            rightCount = n - index - 1
            if rightCount == 1:
                rightSum = val - 1
            else:
                rightNeededCt = val - 1
                if rightCount >= rightNeededCt:
                    if rightNeededCt == 1:
                        rightSum = val-1  + (rightCount - rightNeededCt)
                    else:
                        rightSum = ((val-1 + 1) *(rightNeededCt/2)) + (rightCount - rightNeededCt)
                else:
                    rightSum = (val-1 + val - rightCount) * (rightCount/2)
            
            leftCount = index
            if leftCount == 1:
                leftSum = val - 1
            else:
                leftNeededCt = val - 1
                if leftCount >= leftNeededCt:
                    if leftNeededCt == 1:
                        leftSum = val-1 + (leftCount - leftNeededCt)
                    else:
                        leftSum = ((val-1 + 1) * (leftNeededCt/2)) + (leftCount - leftNeededCt)
                else:
                    leftSum = (val-1 + val - leftCount) * (leftCount / 2)
            
            #print(leftSum, val, rightSum)
            return leftSum + val + rightSum <= maxSum
        
        low = 1
        high = maxSum

        while low < high:
            mid = ceil(low + (high - low) / 2)
            if check(mid):
                low = mid
            else:
                high = mid - 1

        return low
        