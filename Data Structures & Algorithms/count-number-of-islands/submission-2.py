class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        islands = 0

        dirs = [(-1,0), (1, 0), (0,1), (0,-1)]
        visited = set()
        def dfs(r,c):
            if (r <0 or c<0 or r>=rows or c>=cols or grid[r][c] != '1' or (r,c) in visited):
                return
            visited.add((r,c))
            for nd, nc in dirs:
                dfs(r+nd, c+nc)

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1' and (row,col) not in visited:
                    islands +=1
                    dfs(row, col)
        return islands



                
