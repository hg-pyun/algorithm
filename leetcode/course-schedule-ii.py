import queue

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for i in range(numCourses)]
        in_degree = [0 for i in range(numCourses)]
        q = queue.Queue()
        result = []
        
        for x, y in prerequisites:
            graph[y].append(x)
            in_degree[x] += 1
        
        for i in range(len(in_degree)):
            if in_degree[i] == 0:
                q.put(i)
        
        for i in range(numCourses):
            if q.empty():
                return []
            
            v = q.get()
            result.append(v)
            
            for nv in graph[v]:
                in_degree[nv] -= 1
                
                if in_degree[nv] == 0:
                    q.put(nv)
        
        return result
