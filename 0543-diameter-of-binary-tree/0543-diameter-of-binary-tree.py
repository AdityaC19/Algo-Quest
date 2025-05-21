# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxDiameter = 0

        def dfs(node):
            nonlocal maxDiameter
            if not node:
                return 0
            
            left_subtree = dfs(node.left)
            right_subtree = dfs(node.right)
            diameter = left_subtree + right_subtree
            maxDiameter = max(maxDiameter, diameter)

            return 1 + max(left_subtree, right_subtree)
        
        dfs(root)
        return maxDiameter
        