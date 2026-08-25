"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        
        q = deque([root])
        depth = 0

        while q:
            depth += 1
            for _ in range(len(q)):
                node = q.popleft()
                for child in node.children:
                    if child:
                        q.append(child)
                

        return depth


            # maxDepth =0

            # if not root:
            #     return 0
            
            # for child in root.children:
            #     depth = self.maxDepth(child)
            #     maxDepth = max(maxDepth, depth)

            # return 1 + maxDepth    
       