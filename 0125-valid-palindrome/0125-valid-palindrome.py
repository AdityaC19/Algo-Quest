class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_str = ''.join(char for char in s.lower() if char.isalnum())
        
        n = len(cleaned_str)

        def check(i):
            if i >= n//2:
                return True
            
            if cleaned_str[i] != cleaned_str[n-i-1]:
                return False
            
            return check(i+1)
        
        return check(0)



        