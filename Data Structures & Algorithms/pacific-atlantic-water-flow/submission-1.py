class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        m, n = len(heights), len(heights[0])
        res = []
        pac = set()
        atl = set()

        def dfs(r, c, visit, prevHeight):
            if (r, c) in visit or r < 0 or c < 0 or r >= m or c >= n or heights[r][c] < prevHeight:
                return
            visit.add((r, c))
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
        
        for r in range(m):
            dfs(r, 0, pac, 0)
            dfs(r, n - 1, atl, 0)
        
        for c in range(n):
            dfs(0, c, pac, 0)
            dfs(m - 1, c, atl, 0)

        for r in range(m):
            for c in range(n):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r ,c])

        return res