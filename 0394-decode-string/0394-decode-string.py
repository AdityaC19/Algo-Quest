class Solution:
    def decodeString(self, s: str) -> str:
        stk = [] # (temp, num)
        num = 0
        temp = ""

        for i in s:
            if i.isdigit():
                num = (num * 10) + int(i)
            elif i == '[':
                stk.append((temp, num))
                temp = ""
                num = 0
            elif i == ']':
                string, n = stk.pop()
                temp = string + (temp * n)   
                
            else:
                temp += i

        return temp       