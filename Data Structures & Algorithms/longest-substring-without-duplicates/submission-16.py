class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        track = set()

        res = 0

        for r in range(len(s)):
            if s[r] in track:
                res = max(res, r - l)
                while s[r] in track:
                    track.remove(s[l])
                    l +=1
            track.add(s[r])
        
        res = max(res, len(track))

        return res