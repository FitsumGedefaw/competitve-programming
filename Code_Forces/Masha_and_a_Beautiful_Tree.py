t = int(input())

for _ in range(t):
    m = int(input())
    P = [int(num) for num in input().split()]

    minNumOfOps = [0]

    def helper(arr, left, right, res):
        if left == right:
            return [arr[left]]
        
        mid = (left + right)// 2

        leftArr = helper(arr, left, mid, res)
        rightArr = helper(arr, mid+1, right, res)

        if leftArr[0] > rightArr[0]:
            res[0] += 1
            return rightArr + leftArr
        
        return leftArr + rightArr
    
    res = helper(P, 0, len(P)-1, minNumOfOps)

    print(minNumOfOps[0] if res == [i for i in range(1, m+1)] else -1)


    

        
    


