class Solution:
    def subsetsHelper(self, i, arr, currSubset, subsets):
        if i >= len(arr):
            subsets.append(deepcopy(currSubset))
            return
        
        currSubset.append(arr[i])
        self.subsetsHelper(i+1, arr, currSubset, subsets)
        
        currSubset.pop()
        self.subsetsHelper(i+1, arr, currSubset, subsets) 
           
    def subsets(self, nums: List[int]) -> List[List[int]]:
        currSubset, allSubsets = [], []
        self.subsetsHelper(0, nums, currSubset, allSubsets)
        return allSubsets
        
        