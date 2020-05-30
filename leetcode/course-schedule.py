import queue

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for i in range(numCourses)]
        in_degree = [0 for i in range(numCourses)]
        q = queue.Queue()
        
        for x, y in prerequisites:
            graph[y].append(x)
            in_degree[x] += 1
        
        for i in range(len(in_degree)):
            if in_degree[i] == 0:
                q.put(i)
        
        for i in range(numCourses):
            if q.empty():
                return False
            
            v = q.get()
            
            for nv in graph[v]:
                in_degree[nv] -= 1
                
                if in_degree[nv] == 0:
                    q.put(nv)
        
        return True
