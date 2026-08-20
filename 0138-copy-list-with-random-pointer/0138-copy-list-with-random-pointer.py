"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head
        hmap = {}

        if not head: return None

        while curr:
            node = Node(curr.val)
            hmap[curr] = node
            curr = curr.next
        
        curr = head

        while curr:
            new_node = hmap[curr]
            
            new_node.next = hmap[curr.next] if curr. next else None
            new_node.random = hmap[curr.random] if curr.random else None

            curr = curr.next
        
        return hmap[head]

