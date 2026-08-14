# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        isBST = True
        prev = None

        def dfs(node):
            nonlocal isBST, prev
            if not node:
                return 0 
            
            dfs(node.left)
            if prev is not None:
                if node.val <= prev:
                    isBST = False
            prev = node.val
            dfs(node.right)
        
        dfs(root)
        return isBST

        