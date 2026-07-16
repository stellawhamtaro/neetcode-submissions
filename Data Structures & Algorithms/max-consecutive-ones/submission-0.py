class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        streakCount = 0
        longestStreak = 0
        for i in range(len(nums)):
            if nums[i]==1:
                streakCount += 1
            else:
                longestStreak = max(longestStreak, streakCount)
                streakCount = 0
        longestStreak =max(longestStreak, streakCount)
        return longestStreak



