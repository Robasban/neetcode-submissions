class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0

        l, r = 0, 1

        while l < len(s):
            currRep = 0
            while currRep <= k and r < len(s):
                if s[l] != s[r]:
                    if currRep == k:
                        r -= 1
                    currRep += 1
                r += 1
            res = max(res, r - l)
            while l + 1 < len(s) and s[l] == s[l + 1]:
                l += 1
            l += 1

        return res