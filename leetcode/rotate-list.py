# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if head is None:
            return head

        p = head
        length = 1
        while p.next:
            length += 1
            p = p.next
        
        p.next = head
        
        n = length - (k % length)
    
        last = None
        p = head
        
        while n > 0:
            n -= 1
            last = p
            p = p.next
        
        last.next = None
        
        return p
