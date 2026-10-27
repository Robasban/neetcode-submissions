class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        m, n = len(grid), len(grid[0])
        self.total = -1

        def bfs(q):
            qLen = len(q)

            for i in range(qLen):
                r, c = q.popleft()
                if r > 0 and grid[r - 1][c] == 1:
                    grid[r - 1][c] = 2
                    q.append((r - 1, c))
                if r < m - 1 and grid[r + 1][c] == 1:
                    grid[r + 1][c] = 2
                    q.append((r + 1, c))
                if c > 0 and grid[r][c - 1] == 1:
                    grid[r][c - 1] = 2
                    q.append((r, c - 1))
                if c < n - 1 and grid[r][c + 1] == 1:
                    grid[r][c + 1] = 2
                    q.append((r, c + 1))

            self.total += 1
            if q:
                bfs(q)
        
        q = collections.deque()

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:
                    q.append((r, c))

        bfs(q)

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    return -1

        return self.total