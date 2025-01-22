# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = []
        def helper(root):
            if not root:
                return 0
            
            left = helper(root.left)
            ans.append(root.val)
            right = helper(root.right)

        helper(root)
        return ans[k-1]
        
        
        # q = deque([root])
        # ans = []

        # while q:
        #     cur_min = float('inf')
        #     for _ in range(len(q)):
        #         node = q.popleft()
        #         if node.val < cur_min:
        #             cur_min = node.val
        #         #ans.append(node.val)
        #         if node.left: q.append(node.left)
        #         if node.right: q.append(node.right)
        #     ans.append(cur_min)        

        