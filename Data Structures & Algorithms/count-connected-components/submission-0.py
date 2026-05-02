class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjlist = [[] for _ in range(n)]
        visited = [False] * n
        components = 0

        for u, v in edges:
            adjlist[u].append(v)
            adjlist[v].append(u)

        def dfs(node):
            for nei in adjlist[node]:
                if not visited[nei]:
                    visited[nei] = True
                    dfs(nei)

        res = 0
        for node in range(n):
            if not visited[node]:
                visited[node] = True
                dfs(node)
                components +=1
        
        return components

