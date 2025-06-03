"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        q = deque([root])
        res = []
        
        while q:
            cur_level = []
            q_len = len(q)
            for _ in range(q_len):
                node = q.popleft()
                if q_len > 1:
                    node.next = q[0]
                q_len -= 1
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        
        return root





        
        


        