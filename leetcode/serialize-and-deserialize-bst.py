# Definition for a binary tree node.
class Codec:

    def serialize(self, root: TreeNode) -> str:
        def levelOrder(node):
            queue = [node]
            values = []
            lastExistNodeIndex = 0
            index = 0
            while queue:
                currentNode = queue.pop(0)
                if currentNode:
                    lastExistNodeIndex = index + 1
                    values.append(currentNode.val)
                    queue.append(currentNode.left)
                    queue.append(currentNode.right)
                else:
                    values.append(None)
                index += 1
            return values[:lastExistNodeIndex]

        valueArr = levelOrder(root)
        return str(valueArr)

    def deserialize(self, data: str) -> TreeNode:
        treeNodes = [TreeNode(val) if val is not None else None for val in eval(data)]
        if not treeNodes:
            return None

        root = treeNodes.pop(0)
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node:
                if treeNodes:
                    node.left = treeNodes.pop(0)
                    queue.append(node.left)
                if treeNodes:
                    node.right = treeNodes.pop(0)
                    queue.append(node.right)
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
