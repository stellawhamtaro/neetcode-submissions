class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        #go backwards, go until the first space, and return the length
        #from that space to the end. If there is no space, return the length
        # of the entire string.
        phrases = s.split()
        return len(phrases[-1])
