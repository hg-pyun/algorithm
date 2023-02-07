# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        def postorder(node, arr):
            if node is None:
                return

            node.left and postorder(node.left, arr)
            node.right and postorder(node.right, arr)
            
            arr.append(node.val)

        postorder(root, ans)
        
        return ans
