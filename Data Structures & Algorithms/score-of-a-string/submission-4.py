class Solution:
    def scoreOfString(self, s: str) -> int:
        runningsum = 0
        for i in range(0, len(s)-1, 1):
            runningsum = runningsum+abs(ord(s[i])-ord(s[i+1]))
        return runningsum