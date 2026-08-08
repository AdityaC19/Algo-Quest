class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        num_set = set(nums)

        for num in num_set:
            if (num-1) not in num_set:
                current_streak = 1
                current =  num

                while current + 1 in num_set:
                    current_streak += 1
                    current += 1
                longest = max(current_streak, longest)
        
        return longest

                

                

        