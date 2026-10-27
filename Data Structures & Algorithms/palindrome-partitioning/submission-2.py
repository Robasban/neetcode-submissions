class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        res = []
        subset = []

        def backtrack(start):
            if start == len(s):
                res.append(subset.copy())
                return

            for end in range(start + 1, len(s) + 1):
                part = s[start:end]

                if part == part[::-1]:
                    subset.append(part)
                    backtrack(end)
                    subset.pop()


        backtrack(0)
        
        return res