class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        #keep a running count of how many ones seen 
        streak = 0
        longestStreak = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                streak += 1
            else:
                streak = 0
            longestStreak = max(longestStreak, streak)
        return longestStreak
        