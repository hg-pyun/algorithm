"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':        
        visited = {}
        
        def dfs(node):
            if node is None:
                return None
            
            if node in visited:
                return visited[node]
            
            visited[node] = Node(node.val)
            new_neighbors = []
            for neighbor in node.neighbors:
                new_neighbors.append(dfs(neighbor))

            visited[node].neighbors = new_neighbors
            return visited[node]
        
        return dfs(node)
