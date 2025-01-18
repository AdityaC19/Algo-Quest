# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = list1
        curr2 = list2

        if not list1:
            return list2
        if not list2:
            return list1

        dummy = ListNode()
        pointer = dummy

        while curr1 and curr2:
            if curr2.val <= curr1.val:
                pointer.next = curr2
                curr2 = curr2.next 
            else:
                pointer.next = curr1
                curr1 = curr1.next
            pointer = pointer.next
        
        pointer.next = curr1 if curr1 else curr2        
        return dummy.next


            
        
        
