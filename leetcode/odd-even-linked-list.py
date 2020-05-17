# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        
        if head is None:
            return head
        
        p = head
        last_before = p
        even_head = head.next
        c = 0
        
        while (p.next != None):
            
            if p.next.next is None:
                last_before = p
            
            temp = p.next
            p.next = p.next.next
            p = temp
            c += 1

        if c % 2 == 0:
            p.next = even_head
        else:
            last_before.next = even_head
            
        
        return head
