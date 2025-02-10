# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        stk = []
        stk.append(root)

        # while stk:
        #     curSum = 0
        #     for _ in range(len(stk)):
        #         node = stk.pop()
        #         curSum += node.val
        #         #print(node.val, curSum)
        #         if node.left:
        #             stk.append(node.left)
        #         if node.right:
        #             stk.append(node.right)
        #         curSum += node.val
        #         #hmap[curSum] += 1

        # print(hmap)
        if not root:
            return []
        
        sum_freq = defaultdict(int)
        
        def dfs(node):
            if not node:
                return 0
            left_sum = dfs(node.left)
            right_sum = dfs(node.right)
            total_sum = left_sum + right_sum + node.val  
            sum_freq[total_sum] += 1
            return total_sum

        dfs(root)
        print(sum_freq)

        max_freq = max(sum_freq.values())
        result = [] 

        for s, freq in sum_freq.items():
            if freq == max_freq:
                result.append(s)

        return result
