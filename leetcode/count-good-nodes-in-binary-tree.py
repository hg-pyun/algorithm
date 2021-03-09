# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = 0
        def traversal(node, max_val):
            if max_val <= node.val:
                nonlocal ans
                ans += 1
            new_max_val = max(node.val, max_val)
            node.left and traversal(node.left, new_max_val)
            node.right and traversal(node.right, new_max_val)
        traversal(root, root.val)
        return ans
