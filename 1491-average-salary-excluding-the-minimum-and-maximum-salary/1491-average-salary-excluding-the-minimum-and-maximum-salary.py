class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        
        totalSum = 0 
        
        for i in range(1, len(salary)-1): 
            totalSum += salary[i]
            
        return totalSum/(len(salary)-2)
        