#User function Template for python3

class Solution: 
    def select(self, arr, i):
        # code here 
        minValIdx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[minValIdx]:
                minValIdx = j
               
        return minValIdx
    
    def selectionSort(self, arr,n):
        #code here
        for i in range(n):
            minValIdx = self.select(arr, i)
            arr[i], arr[minValIdx] = arr[minValIdx], arr[i]  
