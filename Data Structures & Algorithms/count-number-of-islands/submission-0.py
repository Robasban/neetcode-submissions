class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()

        rows = len(grid)
        cols = len(grid[0])

        def bfs(row, col):
            if (row, col) in visited:
                return
            visited.add((row, col))
            if grid[row][col] == "0":
                return
            if row > 0:
                bfs(row - 1, col)
            if row < rows - 1:
                bfs(row + 1, col)
            if col > 0:
                bfs(row, col - 1)
            if col < cols - 1:
                bfs(row, col + 1)

        islands = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    islands += 1
                    bfs(r, c)
        
        return islands
