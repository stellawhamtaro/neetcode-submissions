class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}  # num -> index
        
        for i, num in enumerate(nums):
            complement = target - num  # What number do we need?
            
            if complement in seen:  # Have we seen it before?
                return [seen[complement], i]  # Return both indices
            
            seen[num] = i  # Store this number for future lookups