# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        if head is None:
            return head
        
        current = head
        current_prev = ListNode(None, current)
        prev = current_prev
        
        while current:
            if current.val == val:
                current_prev.next = current.next
            else:
                current_prev = current
            
            current = current.next
        
        return prev.next     
