class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nexGreaEle = {}
        st = []
        
        for num in nums2:
            while st and st[-1] < num:
                nexGreaEle[st.pop()] = num
                
            st.append(num)
            
        while st:
            nexGreaEle[st.pop()] = -1
            
        for i in range(len(nums1)):
            nums1[i] = nexGreaEle[nums1[i]]
            
        return nums1
        
            