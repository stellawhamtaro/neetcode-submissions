class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        for i in range(len(words)):
            col_width = len(words[i])
            if len(words)<col_width:
                return False
            for j in range(col_width):
                if len(words[j])<=i:
                    return False
                if words[i][j] != words[j][i]:
                    return False 
        return True
