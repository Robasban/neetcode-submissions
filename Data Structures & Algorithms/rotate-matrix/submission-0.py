class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        cRange = n // 2 if n % 2 == 0 else n // 2 + 1
        for r in range(n // 2):
            for c in range(cRange):
                old = matrix[r][c]
                for i in range(4):
                    temp = matrix[c][n - r - 1]
                    matrix[c][n - r - 1] = old
                    old = temp
                    r, c = c, n - r - 1