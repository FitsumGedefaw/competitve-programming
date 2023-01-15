class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        
        d = collections.defaultdict(int)
        def find(number, domain_parent):
            ans = []
            d[domain_parent] += number
            ans.append(domain_parent)
            for idx, i in enumerate(domain_parent):
                if i == '.':
                    d[domain_parent[idx+1:]] += number
                    ans.append(domain_parent[idx+1:])
                    

            return ans
        
        res = []
        for dom in cpdomains:
            dom = dom.split(" ")
            lst = find(int(dom[0]), dom[1])

            
        for key, val in d.items():
            s = str(val) + " " + str(key)
            res.append(s)
            
        return (res)