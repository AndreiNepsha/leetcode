class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        indegree = [0] * numCourses

        graph = [[] for _ in range(numCourses)]
        for p in prerequisites:
            graph[p[1]].append(p[0])
            indegree[p[0]] += 1
        
        q = [i for i in range(numCourses) if not indegree[i]]

        while q:
            i = q.pop()
            for n in graph[i]:
                indegree[n] -= 1
                if not indegree[n]:
                    q.append(n)
        
        return not any(indegree)
