# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        def dfs(node, curMax):
            nonlocal count
            if not node:
                return None
            
            curMax = max(curMax, node.val)

            if node.val >= curMax:
                count += 1
            
            left = dfs(node.left, curMax)
            right = dfs(node.right, curMax)
        
            return left or right
        dfs(root,float('-inf'))
        return count