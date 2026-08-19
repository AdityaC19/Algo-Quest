class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_str = str(x)

        l = 0 
        r = len(x_str) - 1

        while l <= r:
            if x_str[l] != x_str[r]:
                return False
            l += 1
            r -= 1
        
        return True