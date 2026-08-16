# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque([root])
        ans = []
        flip = 0

        if not root:
            return []

        while q:
            curr_level = []
            for _ in range(len(q)):
                node = q.popleft()
                curr_level.append(node.val)
                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)
            flip ^= 1
            ans.append(curr_level) if flip == 0 else ans.append(curr_level[::-1])
        
        return ans
        