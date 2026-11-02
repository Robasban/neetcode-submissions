class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = []
        for _ in range(m):
            grid.append([0] * n)
        grid[0][0] = 1
        for r in range(m):
            for c in range(n):
                if r == 0 and c == 0:
                    continue
                val = 0
                if r > 0:
                    val += grid[r - 1][c]
                if c > 0:
                    val += grid[r][c - 1]
                grid[r][c] = val
        
        return grid[-1][-1]