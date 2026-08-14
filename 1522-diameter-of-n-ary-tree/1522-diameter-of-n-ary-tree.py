"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """
        diameter = 0

        def dfs(node):
            nonlocal diameter

            if not node:
                return 0

            maxDepth = 0
            for child in node.children:
                depth = dfs(child)
                diameter = max(diameter, depth + maxDepth)
                maxDepth = max(maxDepth, depth)
            
            return 1 + maxDepth
        
        dfs(root)
        return diameter
            




            

            


            
