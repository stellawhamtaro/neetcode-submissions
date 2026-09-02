class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #make a check whether they are the same length
        if len(s) != len(t):
            return False
        #for each character in s, add it to a dictionary that has the key of the letter, and the value of the count. 
        s_dict = {}
        for char in s:
            s_dict[char] = s_dict.get(char,0)+1 #find char, if doesnt exist, default 0 

        for char in t:
            if char not in s_dict:
                return False 
            else:
                s_dict[char] -= 1
                if s_dict[char] < 0:
                    return False
        return True 


