# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            head = None
            return head
                    
        fast = slow = head

        while fast and fast.next:
            slow_val = slow.val
            fast = fast.next.next
            slow = slow.next
        
        if(slow.next):
            slow.val = slow.next.val
            slow.next = slow.next.next 
        else:
            head.next = None
        
        return head


        