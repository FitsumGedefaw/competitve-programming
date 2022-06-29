class Solution: 
    def select(self, arr, i):
        if arr[i : ]:
            return min(arr[i : ])
    
    def selectionSort(self, arr,n):
        for i in range(n):
            selected = self.select(arr, i)
            min_index = arr[i : ].index(selected) + i
            if arr[i] > arr[min_index]:
                temp = arr[min_index]
                arr[min_index] = arr[i]
                arr[i] = temp
        return arr
