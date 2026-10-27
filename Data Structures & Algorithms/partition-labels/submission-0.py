class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastOccurance = dict()

        for i in range(len(s)):
            lastOccurance[s[i]] = i

        start = 0
        goUntil = lastOccurance[s[0]]
        res = []

        for i in range(len(s)):
            goUntil = max(goUntil, lastOccurance[s[i]])
            if i == goUntil:
                res.append(goUntil - start + 1)
                start = goUntil + 1
                goUntil = float('-inf')
        
        return res