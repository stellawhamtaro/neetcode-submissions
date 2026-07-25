class Solution:    
    def isValid(self, s: str) -> bool:
        ListofChar = []
        for i in range(len(s)):
            if (s[i] == '(' or s[i] == '{' or s[i] == '['):
                ListofChar.append(s[i])
            else:
                if not ListofChar:
                    return False
                top = ListofChar.pop()
                if top == '[':
                    if s[i] != ']':
                        return False
                elif top == '{':
                    if s[i] != '}':
                        return False
                elif top == '(':
                    if s[i] != ')':
                        return False
        return len(ListofChar) == 0