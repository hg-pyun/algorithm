# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None:
            return False
        
        one = head
        two = head.next
        
        while one != two:
            if two is None or two.next is None:
                return False
            
            one = one.next
            two = two.next.next
        
        return True
