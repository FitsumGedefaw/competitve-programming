class Solution:
    def maxLength(self, arr: List[str]) -> int:
        ans = 0
        
        def backtrack(curr, i):
            nonlocal ans
            
            if i == len(arr):
                conc = ""
                for s in curr:
                    conc += s
                
                if len(conc) == len(set(conc)):
                    #print(conc, set(conc))
                    ans = max(ans, len(conc))
                return
            
            curr.append(arr[i])
            backtrack(curr, i + 1)
            curr.pop()
            backtrack(curr, i + 1)
            
        backtrack([], 0)
        return ans
        