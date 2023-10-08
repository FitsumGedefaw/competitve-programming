class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        # Initialize the result variable
        result = 0
        
        # Iterate over all possible prefixes of the binary representation of the numbers in the given list
        for i in range(32)[::-1]:
            # Calculate the maximum XOR of any two numbers in the list that have the current prefix
            result <<= 1
            prefix_set = {num >> i for num in nums}
            result += any(result^1 ^ p in prefix_set for p in prefix_set)
        
        # Return the result
        return result