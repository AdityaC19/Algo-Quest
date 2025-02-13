# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque([root])
        ans = []

        flag = 0

        if not root: return []

        while q:
            curr_level = []
            for _ in range(len(q)):
                node = q.popleft()
                curr_level.append(node.val)
                print(curr_level, flag)
                if node.left: 
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if flag == 1:
                curr_level.reverse()
            flag ^= 1
            ans.append(curr_level)
        
        return ans


