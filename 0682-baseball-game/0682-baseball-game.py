class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stk = []

        for ops in operations:
            if ops not in 'CD+':
                stk.append(int(ops))
                #print(stk)
            elif ops == 'D':
                y = int(stk[-1]) * 2
                stk.append(y)
            elif ops == 'C':
                stk.pop()
                #print(stk)
            else:
                x = int(stk[-1]) + int(stk[-2])
                stk.append(x)
        
        res = 0
        for s in stk:
            res += s
        
        return res
        
     
        

