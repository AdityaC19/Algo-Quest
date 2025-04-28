# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []

        for i, node in enumerate(lists):
            if node:
                heapq.heappush(min_heap, (node.val, i, node))
        
        D = ListNode()
        curr = D

        while min_heap:
            val, i, node = heapq.heappop(min_heap)
            curr.next = node
            curr = curr.next
            node = node.next
            if node:
                heapq.heappush(min_heap, (node.val, i, node))
        
        return D.next
