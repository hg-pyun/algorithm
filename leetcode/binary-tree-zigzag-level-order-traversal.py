# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if root is None:
            return []
        
        def height(node):
            if node is None:
                return 0
            else:
                lheight = height(node.left)
                rheight = height(node.right)
                
                if lheight > rheight:
                    return lheight + 1
                else:
                    return rheight + 1
            
        def traversal(node, level, larr):
            if node is None:
                return;
            if level == 1:
                larr.append(node.val)
            elif level > 1:
                traversal(node.left, level - 1, larr)
                traversal(node.right, level - 1, larr)
                
        ans = []
        h = height(root)
        
        for i in range(h):
            larr = []
            traversal(root, i+1, larr)
            ans.append(larr if i%2 == 0 else list(reversed(larr)))
            
        return ans
