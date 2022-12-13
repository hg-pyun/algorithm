# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        ans = []

        def dfs(node, path, targetSum):
            if node is None:
                return

            path.append(node.val)

            if node.left is None and node.right is None:
                print(path)
                if sum(path) == targetSum:
                    ans.append(path)
            
            node.left and dfs(node.left, copy.deepcopy(path), targetSum)
            node.right and dfs(node.right, copy.deepcopy(path), targetSum)
        
        dfs(root, [], targetSum)

        return ans
