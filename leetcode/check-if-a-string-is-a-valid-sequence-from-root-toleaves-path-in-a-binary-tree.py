# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:    
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        self.target = "".join(map(str, arr))
        self.result = False
        self.traversal(root, [])
        return self.result
    def traversal(self, node, path):
        if node is None:
            return
        path.append(node.val)
        if node.left is None and node.right is None:
            check = "".join(map(str, path)) == self.target
            if check:
                self.result = check
            return
        self.traversal(node.left, copy.deepcopy(path))
        self.traversal(node.right, copy.deepcopy(path))
