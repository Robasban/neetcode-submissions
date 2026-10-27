class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        passed = set()
        m, n = len(board), len(board[0])

        def backtrack(index, row, col):
            if index == len(word):
                return True

            if row < 0 or row >= m or col < 0 or col >= n:
                return False

            if (row, col) in passed:
                return False
            
            if board[row][col] != word[index]:
                return False

            passed.add((row, col))
            
            found = backtrack(index + 1, row - 1, col) or backtrack(index + 1, row + 1, col) or backtrack(index + 1, row, col - 1) or backtrack(index + 1, row, col + 1)
            
            passed.remove((row, col))

            return found

        for r in range(len(board)):
            for c in range(len(board[r])):
                if backtrack(0, r, c):
                    return True
                       
        return False