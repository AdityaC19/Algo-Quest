class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        n = len(nums)
        
        max_length = 0

        for num in s:
            if num-1 not in s:
                length = 1
                next_num = num+1
                while next_num in s:
                        length += 1
                        next_num += 1
                max_length = max(max_length, length)
        
        return max_length






        




