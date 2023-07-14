class Solution:
    def eventualSafeNodes(self, graph: list[list[int]]) -> list[int]:
        visited = [0] * len(graph)

        VISITED, NOT_SAFE, SAFE = 1, 2, 3

        def find_safe(i):
            if visited[i]:
                return
            
            visited[i] = VISITED

            safe = SAFE
            for n in graph[i]:
                find_safe(n)
                if visited[n] < 3:
                    safe = NOT_SAFE
            visited[i] = safe
        
        for i in range(len(graph)):
            find_safe(i)
        
        return [i for i in range(len(graph)) if visited[i] == SAFE]
