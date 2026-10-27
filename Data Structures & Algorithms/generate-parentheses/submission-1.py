class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        s = ''

        def backtrack(o, c, s):
            if c > o or c > n or o > n:
                return
            if len(s) == 2 * n and o == c:
                res.append(s)
                return
            s += '('
            backtrack(o + 1, c, s)
            s = s[:-1]
            s += ')'
            backtrack(o, c + 1, s)

        backtrack(0, 0, s)

        return res