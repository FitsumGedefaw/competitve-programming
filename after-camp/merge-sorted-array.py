class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m-1
        j = n-1
        
        for insertIdx in range(m+n-1, -1, -1):
            if i > -1 and j > -1:
                
                if nums1[i] > nums2[j]:
                    nums1[insertIdx] = nums1[i]
                    i -= 1
                
                else:
                    nums1[insertIdx] = nums2[j]
                    j -= 1
                    
            elif i > -1:
                nums1[insertIdx] = nums1[i]
                i -= 1
                
            else:
                nums1[insertIdx] = nums2[j]
                j -= 1
                
                    
            
        
        
    
        
            
        
