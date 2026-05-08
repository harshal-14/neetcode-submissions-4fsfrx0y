class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pre_map = {c: [] for c in range(numCourses)}
        visited = set()
        visiting = set()

        output = []
        for pre, crs in prerequisites:
            pre_map[pre].append(crs)

        def dfs(node):
            if node in visiting:
                return False
            if node in visited:
                return True
            visiting.add(node)
            for nei in pre_map[node]:
                if not dfs(nei): return False
            visiting.remove(node)
            visited.add(node)
            output.append(node)
            return True
        
        for i in range(numCourses):
            if not dfs(i): return []

        return output