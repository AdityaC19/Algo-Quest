class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        hmap = {'(':')', '[':']', '{':'}'}

        for i in s:
            if i in hmap:
                stk.append(i)
            elif stk and i == hmap[stk[-1]]:
                stk.pop()
            else:
                return False
        return not stk
        