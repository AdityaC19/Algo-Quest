# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque([root])
        res = []

        if not root:
            return []
        while q:
            cur_level = []
            for _ in range(len(q)):
                node = q.popleft()
                cur_level.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            res.append(cur_level)
        return res

