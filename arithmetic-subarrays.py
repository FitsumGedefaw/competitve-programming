class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        answer = []
        for i in range(len(r)):
            subArr = nums[l[i]: r[i]+1]
            subArr.sort()
            diff = subArr[1] - subArr[0]
            booll = True
            for j in range(1, len(subArr)-1):
                if (subArr[j+1] - subArr[j]) != diff:
                    booll = False
            answer.append(booll)
        return answer
            
        
        
