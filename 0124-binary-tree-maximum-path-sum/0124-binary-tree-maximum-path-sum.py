# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxx = [float('-inf')]
        def dfs(node):
            if not node:
                return 0
            
            left_tree = max(dfs(node.left), 0)
            right_tree = max(dfs(node.right), 0)
            max_path = left_tree + right_tree + node.val
            maxx[0] = max(maxx[0], max_path)

            return node.val + max(left_tree, right_tree)
        
        dfs(root)
        return maxx[0]



        