class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_str = ''.join(char for char in s.lower() if char.isalnum())
        return cleaned_str == cleaned_str[::-1]



        


        