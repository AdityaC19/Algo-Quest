class Solution:
    def isPalindrome(self, s: str) -> bool:
        cstr = []
        for i in s:
            if i.isalnum():
                cstr.append(i.lower())
        
        clean_str = "".join(cstr)

        l = 0
        r = len(clean_str)-1

        while l <= r:
            if clean_str[l] != clean_str[r]:
                return False
            l+=1
            r-=1
        
        return True
        