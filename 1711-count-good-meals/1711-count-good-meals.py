from collections import Counter

class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        def largest_power_of_2(num):
			
			
            num = '1' + '0' * len('{:b}'.format(num))
            return int(num, 2)   
            
        res = 0
        good_pairs = Counter(deliciousness) 
        num_of_0 = good_pairs[0] 
        for meal1, num1 in good_pairs.items():
            largest_power = largest_power_of_2(meal1)
            meal2 = largest_power - meal1
            
            if meal2 > meal1:
				
                continue
            elif meal2 in good_pairs:
                num2 = good_pairs[meal2]
                if meal1 == meal2:
			
                    res += num1 * (num2 - 1) // 2 
                    res += num_of_0 * num1 
                else:
					# If the number is not the power of two, just multiple amounts of meal1 and its good pair.
                    res += num1 * num2
            
        return res % (10**9 +7)