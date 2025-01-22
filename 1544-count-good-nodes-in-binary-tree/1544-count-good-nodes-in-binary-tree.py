# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0

        def isGood(root, current_max):
            nonlocal count
            if not root:
                return 0
            
            if current_max <= root.val:
                current_max = root.val
                count += 1
            
            isGood(root.left, current_max)
            isGood(root.right, current_max)

        isGood(root, root.val)
        return count
        
        