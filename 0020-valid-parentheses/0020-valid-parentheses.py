class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        hmap = {')':'(', '}':'{', ']':'['}

        for i in range(len(s)):
            if s[i] not in hmap:
                stk.append(s[i])
            elif stk and hmap[s[i]] == stk[-1]:
                stk.pop()
            else:
                return False
        
        return True if not stk else False