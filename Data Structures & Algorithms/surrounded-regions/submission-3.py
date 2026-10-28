class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        m, n = len(board), len(board[0])


        def bfs(q):
            while q:
                r, c = q.popleft()
                if r < 0 or c < 0 or r >= m or c >= n:
                    continue
                if board[r][c] == "O":
                    board[r][c] = "P"
                    q.append((r - 1, c))
                    q.append((r + 1, c))
                    q.append((r, c - 1))
                    q.append((r, c + 1))

        q = collections.deque()

        for r in range(m):
            if board[r][0] == "O":
                q.append((r, 0))
            if board[r][n - 1] == "O":
                q.append((r, n - 1))
        for c in range(n):
            if board[0][c] == "O":
                q.append((0, c))
            if board[m - 1][c] == "O":
                q.append((m - 1, c))
        
        bfs(q)

        for r in range(m):
            for c in range(n):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "P":
                    board[r][c] = "O"
