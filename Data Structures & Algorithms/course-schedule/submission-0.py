class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        #map each course to its prerequisites
        premap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            premap[crs].append(pre)

        visiting = set()

        def dfs(crs):
            if crs in visiting:
                # cycle detected
                return False

            if premap[crs] == []:
                return True

            visiting.add(crs) #currently visiting this
            for pre in premap[crs]:
                if not dfs(pre): return False

            visiting.remove(crs) #no longer visiting the course
            premap[crs] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
