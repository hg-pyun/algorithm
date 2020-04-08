# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        one = head
        two = head

        while True:
            if two is None or two.next is None:
                return one

            one = one.next
            two = two.next.next
            
