class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 1

        trackChars = set()

        res = 0

        if len(s) == 0:
            return 0
        
        if len(s) == 1:
            return 1

        trackChars.add(s[l])

        while r < len(s):
            if s[r] in trackChars:
                res = max(res, r - l)
                while s[l] != s[r]:
                    trackChars.remove(s[l])
                    l += 1
                trackChars.remove(s[l])
                l += 1
            trackChars.add(s[r])
            r += 1
        
        res = max(res, r - l)

        return res