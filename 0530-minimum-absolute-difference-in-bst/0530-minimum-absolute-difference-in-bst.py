# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        minn = float('inf')
        prev = None
        def dfs(node):
            nonlocal prev, minn
            if not node:
                return 0
            
            dfs(node.left)
            if prev is not None:
                minn = min(minn, node.val - prev)
            prev = node.val
            dfs(node.right)

        
        dfs(root)
        return minn
        


        