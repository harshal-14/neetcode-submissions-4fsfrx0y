class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjlist = [[] for _ in range(n)] # create adj list with array style
        visited = [False] * n # array of size n with all False
        components = 0

        for u, v in edges: # build the adj list
            adjlist[u].append(v)
            adjlist[v].append(u)

        def dfs(node):
            # if visited[node]:
            #     return
            
            for nei in adjlist[node]:
                if not visited[nei]:
                    visited[nei] = True
                    dfs(nei)

        for i in range(n):
            if not visited[i]:
                visited[i] = True
                dfs(i)
                components +=1
        return components
