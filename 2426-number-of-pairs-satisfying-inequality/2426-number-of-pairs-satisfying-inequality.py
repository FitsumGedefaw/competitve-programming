class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        def mergedHelper(arr, left, right, numOfPairs):
            if left == right:
                return [arr[left]]
            
            mid = (left + right)//2
            
            leftArr = mergedHelper(arr, left, mid,numOfPairs)
            rightArr = mergedHelper(arr, mid+1, right, numOfPairs)
            
            i = j = 0
            while j < len(rightArr):
                while i < len(leftArr) and leftArr[i] <= rightArr[j]+diff:
                    i += 1
                numOfPairs[0] += i
                j += 1
            
            return (merge(leftArr, rightArr))
                
        
        def merge(arr1, arr2):
            ptr1 = ptr2 = 0
            res = []
            while ptr1 < len(arr1) or ptr2 < len(arr2):
                if ptr1 < len(arr1) and not ptr2 < len(arr2):
                    res.append(arr1[ptr1])
                    ptr1 += 1
                
                elif not ptr1 < len(arr1) and ptr2 < len(arr2):
                    res.append(arr2[ptr2])
                    ptr2 += 1
                
                else:
                    if arr1[ptr1] < arr2[ptr2]:
                        res.append(arr1[ptr1])
                        ptr1 += 1
                    else:
                        res.append(arr2[ptr2])
                        ptr2 += 1
            return res
                    
            
            
            
        merged = []
        numOfPairs = [0]
        for i in range(len(nums1)):
            merged.append(nums1[i] - nums2[i])
            
        mergedHelper(merged, 0, len(merged)-1, numOfPairs)
        return numOfPairs[0]
        
        
        