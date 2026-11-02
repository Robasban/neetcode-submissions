class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        rowSet, colSet = set(), set()

        for r in range(m):
            if len(rowSet) == m or len(colSet) == n:
                break
            for c in range(n):
                if matrix[r][c] == 0:
                    self.fillSentinel(matrix, r, c)
                    rowSet.add(r)
                    colSet.add(c)

        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 'S':
                    matrix[r][c] = 0
    
    def fillSentinel(self, matrix, r, c):
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            if matrix[i][c] != 0:
                matrix[i][c] = 'S'
        for i in range(n):
            if matrix[r][i] != 0:
                matrix[r][i] = 'S'