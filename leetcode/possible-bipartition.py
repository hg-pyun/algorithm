class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        graph = [[] for i in range(N + 1)]
        
        for [a, b] in dislikes:
            graph[a].append(b)
            graph[b].append(a)
        
        color = {}
        def dfs(node, c = 0):
            if node in color:
                return color[node] == c
            
            color[node] = c
            for neighbor in graph[node]:
                if dfs(neighbor, c ^ 1) is False:
                    return False
            return True
        
        for node in range(1, N + 1):
            if node not in color and dfs(node) is False:
                return False
            
        return True
