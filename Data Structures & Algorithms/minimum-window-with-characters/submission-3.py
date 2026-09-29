class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        tfreq = dict()
        for i in range(len(t)):
            tfreq[t[i]] = 1 + tfreq.get(t[i], 0)
        for i in range(len(t)):
            if s[i] in tfreq:
                tfreq[s[i]] -= 1
        needed = 0
        res = ""
        for v in tfreq.values():
            if v > 0:
                needed += 1
        if needed == 0:
            return s[0:len(t)]
        l = 0
        for r in range(len(t), len(s)):
            if s[r] in tfreq:
                tfreq[s[r]] -= 1
                if tfreq[s[r]] == 0:
                    needed -= 1
            while needed == 0:
                if res == "" or (r - l) < len(res):
                    res = s[l:r + 1]
                if s[l] in tfreq:
                    tfreq[s[l]] += 1
                    if tfreq[s[l]] == 1:
                        needed += 1
                l += 1
        return res

