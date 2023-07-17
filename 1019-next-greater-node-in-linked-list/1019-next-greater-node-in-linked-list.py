# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        nums = [] 
        st = []

        while head:
            nums.append(head.val)
            head = head.next
            
        ans = [0] * len(nums)
        
        for idx, val in enumerate(nums):
            while st and st[-1][1] < val:
                i = st.pop()[0]
                ans[i] = val
               
            st.append((idx, val))
        
        while st:
            i = st.pop()[0]
            ans[i] = 0
        
        return ans
            
        
        
        