class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        #jewel = set(jewels)
        counter = 0

        for stone in stones:
            if stone in jewels:
                counter += 1
        
        return counter