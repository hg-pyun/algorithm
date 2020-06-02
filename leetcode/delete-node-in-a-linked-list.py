# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        p = node
        while p.next != None:
            p.val = p.next.val
            
            if p.next.next == None:
                p.next = None
                break
            
            p = p.next
