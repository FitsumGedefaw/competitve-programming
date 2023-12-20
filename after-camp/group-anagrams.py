class Solution:
    
    #TC: O(nlog(k) + n)     where k = 100
    # SC: O(n) ->for d
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for i in range(len(strs)):
            s = str(sorted(strs[i]))
            d[s].append(i)

        ans = []
        for st in d:
            ans.append([strs[i] for i in d[st]])
        
        return ans
        
        