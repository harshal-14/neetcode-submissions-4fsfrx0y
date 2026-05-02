class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        # Build adjacency list
        adj = {i: [] for i in range(n)}
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visit = set()
        def dfs(parent, node):
            visit.add(node)
            
            for nei in adj[node]:
                if nei == parent:
                    continue  # skip the edge back to parent
                if nei in visit:
                    return False  # cycle detected
                if not dfs(node, nei):
                    return False
            return True

        res = dfs(-1, 0)
        return res and len(visit) == n 

        
            

