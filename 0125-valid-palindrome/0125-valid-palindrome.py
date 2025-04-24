class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_str = ''.join(char for char in s.lower() if char.isalnum())
        
        n = len(cleaned_str)

        l = 0
        r = n-1

        while l <= r:
            if cleaned_str[l] != cleaned_str[r]:
                return False
            
            l += 1
            r -= 1
        
        return True



        


        