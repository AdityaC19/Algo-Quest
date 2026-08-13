# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteNodes(self, head: Optional[ListNode], m: int, n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        curr = dummy

        while curr and curr.next:
            for _ in range(m):
                if curr.next:
                    curr = curr.next
                else:
                    return dummy.next

            for _ in range(n):
                if curr.next:
                    curr.next = curr.next.next
                else:
                    break
                    
        return dummy.next
        


        