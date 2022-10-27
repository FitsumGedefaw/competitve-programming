class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        st = deque()
        n = len(nums) - 1
        for i in range(len(nums)):
            while st and st[-1] > nums[i] and len(st)+(n-i) >= k:
                st.pop()
            st.append(nums[i])
        while len(st) > k:
            st.pop()
        return st