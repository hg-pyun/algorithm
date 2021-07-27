# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        
        temp = head.next
        head.next = temp.next
        temp.next = head
        head.next = self.swapPairs(head.next)
        
        return temp
