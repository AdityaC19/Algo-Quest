class Solution:
    def isValid(self, s: str) -> bool:
        hmap = {')': '(', ']': '[', '}': '{'}

        stk = []

        for i in s:
            if i not in hmap:
                stk.append(i)
            elif stk and stk[-1] == hmap[i]:
                stk.pop()
            else:
                return False

        return not stk
            
        