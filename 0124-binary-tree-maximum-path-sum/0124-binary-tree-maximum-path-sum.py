# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxSum = float('-inf')

        def dfs(node):
            nonlocal maxSum
            if not node:
                return 0
            
            left_subtree = max(dfs(node.left), 0)
            right_subtree = max(dfs(node.right), 0)
            curSum = left_subtree + right_subtree + node.val
            maxSum = max(maxSum, curSum)

            return node.val + max(left_subtree, right_subtree)
        
        dfs(root)
        return maxSum



        