class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        res = 0
        
        skill.sort()
        
        totalSkill = skill[0] + skill[-1]
        
        l, r = 0, len(skill)-1
        
        while l < r:
            if skill[l] + skill[r] == totalSkill:
                res += (skill[l] * skill[r])
                l, r = l+1, r-1
                
            else:
                return -1
        
        return res