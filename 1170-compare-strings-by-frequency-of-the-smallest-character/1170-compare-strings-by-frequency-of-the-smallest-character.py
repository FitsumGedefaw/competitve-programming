class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def f(s):
            freq = Counter(s)
            freq = sorted(freq.items())
            return freq[0][1]
        
        words = [f(w) for w in words]
        words.sort()
        
        for i in range(len(queries)):
            q = f(queries[i])
            
            low, high = 0, len(words)-1
            while low < high:
                mid = low + (high-low)//2
                
                if q < words[mid]:
                    high = mid
                else:
                    low = mid + 1
                
            queries[i] = len(words) - low if words[low] > q else 0
        
        return queries
                
            
        
        