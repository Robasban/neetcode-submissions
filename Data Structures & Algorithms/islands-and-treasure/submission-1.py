class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        m, n = len(grid), len(grid[0])

        def bfs(q):
            while(q):
                r, c = q.popleft()
                if not (0 <= r < m and 0 <= c < n):
                    continue
                if grid[r][c] == -1:
                    continue
                
                if r > 0 and grid[r - 1][c] == 2147483647:
                    grid[r - 1][c] = grid[r][c] + 1
                    q.append((r - 1, c))
                if r < m - 1 and grid[r + 1][c] == 2147483647:
                    grid[r + 1][c] = grid[r][c] + 1
                    q.append((r + 1, c))
                if c > 0 and grid[r][c - 1] == 2147483647:
                    grid[r][c - 1] = grid[r][c] + 1
                    q.append((r, c - 1))
                if c < n - 1 and grid[r][c + 1] == 2147483647:
                    grid[r][c + 1] = grid[r][c] + 1
                    q.append((r, c + 1))

        q = collections.deque()

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    q.append((r, c))

        bfs(q)