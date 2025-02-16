# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_length = [0]
        def dfs(node):
            if not node:
                return 0
            
            left_tree = dfs(node.left)
            right_tree = dfs(node.right)
            diameter = left_tree + right_tree
            max_length[0] = max(max_length[0], diameter)

            return 1 + max(left_tree, right_tree)
        
        dfs(root)
        return max_length[0]

        