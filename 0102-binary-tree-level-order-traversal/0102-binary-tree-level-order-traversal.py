# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque([root])
        level = 0
        ans = []

        
        def _bfs(root, level):
            if not root:
                return 0

            while q:
                for _ in range(len(q)):
                    node = q.popleft()
                    #print(level, node)
                    while len(ans)<=level:
                        ans.append([])
                    ans[level].append(node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                level += 1

        _bfs(root, 0)
        return ans