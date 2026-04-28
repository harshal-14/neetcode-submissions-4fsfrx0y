class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        rows = len(board)
        cols = len(board[0])
        def backtrack(row, col, i):

            if i == len(word):
                return True
            
            if (row<0 or row >= rows or 
            col < 0 or col >= cols or 
            board[row][col] != word[i] or
            (row, col) in visited ):
                return False

            visited.add((row, col))
            for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                if backtrack(row + dr, col + dc, i + 1):
                    return True
            visited.remove((row, col))

        for row in range(rows):
            for col in range(cols):
                if backtrack(row, col, 0):
                    return True
        return False
