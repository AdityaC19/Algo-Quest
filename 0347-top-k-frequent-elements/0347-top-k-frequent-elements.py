class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)

        c_sorted = sorted(c.items(), key= lambda x: x[1], reverse = True)
        
        #print(c_sorted)

        ans = []
        for i in range(k):
            ans.append(c_sorted[i][0])
        
        return ans

        