# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxD = [0]
        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)
            diameter = left + right
            maxD[0] = max(maxD[0], diameter)

            return 1 + max(left, right)

        dfs(root)
        return maxD[0]
        

        