# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        ans = []
        def traversal(node, path):
            if node is None:
                return
            path += str(node.val)
            if node.left is None and node.right is None:
                ans.append(path)
                return
            else:
                path += ','
            traversal(node.left, path)
            traversal(node.right, path)
        traversal(root, "")
        return list(map(lambda item: "->".join(item.split(',')), ans))
