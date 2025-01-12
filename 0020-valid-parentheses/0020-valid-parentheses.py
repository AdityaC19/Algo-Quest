class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        hmap = {']':'[', ')':'(', '}':'{'}

        for i in s:
            if i not in hmap:
                stk.append(i)
            else:
                if not stk:
                    return False
                else:
                    popped = stk.pop()
                    if popped != hmap[i]:
                        return False
        return not stk
                
