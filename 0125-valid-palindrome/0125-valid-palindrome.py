class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_str = ''.join(char for char in s.lower() if char.isalnum())
        
        L = 0
        R = len(cleaned_str)-1

        while L <= R:
            if cleaned_str[L] != cleaned_str[R]:
                return False
            L+=1
            R-=1
        return True


        