class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()

        rows = len(grid)
        cols = len(grid[0])

        def dfs(r, c):
            if ((r not in range(rows)) or (c not in range(cols)) or
                ((r, c) in visited) or 
                (grid[r][c] == 0)):
                return 0
            
            visited.add((r, c))

            return 1 + dfs(r-1, c) + dfs(r+1, c) + dfs(r, c-1) + dfs(r, c+1)


        maxSize = 0

        for row in range(rows):
            for col in range(cols):
                if (row, col) not in visited and grid[row][col] == 1:
                    tempSize = dfs(row, col)
                    if tempSize > maxSize:
                        maxSize = tempSize

        return maxSize

        