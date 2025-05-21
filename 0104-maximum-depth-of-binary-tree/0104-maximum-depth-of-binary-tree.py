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

        if not root:
            return 0

        q = deque([root])

        while q:
            for _ in range(len(q)):
                root = q.popleft()
                if root.left: q.append(root.left)
                if root.right: q.append(root.right)
            level += 1

        return level

        