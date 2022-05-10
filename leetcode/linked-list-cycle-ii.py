# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        visited = set()
        
        while True:
            if head is None:
                return None
            
            if head in visited:
                return head
            
            visited.add(head)
            head = head.next
