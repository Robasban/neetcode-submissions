class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()

        rows = len(grid)
        cols = len(grid[0])

        def bfs(row, col):
            q = collections.deque()

            size = 0

            visited.add((row, col))
            q.append((row, col))

            while q:
                r, c = q.popleft()
                size += 1
                dir = [(1,0), (-1,0), (0,1), (0,-1)]
                for dr, dc in dir:
                    row, col = r + dr, c + dc
                    if (row in range(rows) and
                        col in range(cols) and
                        grid[row][col] == 1 and
                        (row, col) not in visited):
                        q.append((row, col))
                        visited.add((row, col))
                
            return size


        maxSize = 0
        
        for row in range(rows):
            for col in range(cols):
                if (row, col) not in visited and grid[row][col] == 1:
                    tempSize = bfs(row, col)
                    if tempSize > maxSize:
                        maxSize = tempSize

        return maxSize