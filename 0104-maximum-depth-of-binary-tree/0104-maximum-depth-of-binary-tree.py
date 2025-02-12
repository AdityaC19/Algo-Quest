# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        level = 0

        if not root: return 0
        q = deque()
        q.append(root)

        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if node.left: 
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        
        return level

