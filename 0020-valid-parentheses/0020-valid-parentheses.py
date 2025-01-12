class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        hmap = {'(':')', '[':']', '{':'}'}

        for i in s:
            if i in hmap: #Opening bracket
                stk.append(i)
            elif stk and i == hmap[stk[-1]]:  #Closing bracket
                stk.pop()
            else:
                return False
                
        return not stk
                
