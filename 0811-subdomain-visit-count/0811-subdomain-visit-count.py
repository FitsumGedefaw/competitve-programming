class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        subDomains = {}
        
        for subdom in cpdomains:
            rep, domain = subdom.split()
            rep = int(rep)
            
            subDomains[domain] = subDomains.get(domain, 0) + rep
            
            domPartitions = domain.split(".")
            
            sd1 = domPartitions[-1]
            subDomains[sd1] = subDomains.get(sd1, 0) + rep
            
            if len(domPartitions) == 3:
                sd2 = domPartitions[1] + "." + domPartitions[2]
                subDomains[sd2] = subDomains.get(sd2, 0) + rep
                
        res = []
        
        for sd in subDomains:
            rep = str(subDomains[sd])
            
            res.append(rep + " " + sd)
            
        return res
            
                
                
                
                
            
        
        
            