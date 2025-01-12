class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        signs = ('+', '-', '*', '/')
        stk = []
        
        for i in tokens:
            if i not in signs:
                stk.append(i)
            else:
                b, a = stk.pop(), stk.pop()
                res = str(int(eval(a + i + b)))
                stk.append(res)
        
        return int(stk[0])
