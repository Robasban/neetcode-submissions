class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()

        rows = len(grid)
        cols = len(grid[0])

        def bfs(row, col):
            q = collections.deque()

            visited.add((row, col))
            q.append((row, col))

            while q:
                r, c = q.popleft()
                dir = [(1,0), (-1,0), (0,1), (0,-1)]
                for dr, dc in dir:
                    row, col = r + dr, c + dc
                    if (row in range(rows) and
                        col in range(cols) and
                        grid[row][col] == "1" and
                        (row, col) not in visited):
                        q.append((row, col))
                        visited.add((row, col))


        islands = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    islands += 1
                    bfs(r, c)
        
        return islands
