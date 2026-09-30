class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1freq = [0] * 26
        s2freq = [0] * 26
        l = 0
        r = len(s1)
        for c in s1:
            s1freq[ord(c) - 97] += 1
        for i in range(len(s1)):
            s2freq[ord(s2[i]) - 97] += 1
        if s1freq == s2freq:
            return True
        while r < len(s2) - 1:
            s2freq[ord(s2[l]) - 97] -= 1
            s2freq[ord(s2[r]) - 97] += 1
            l += 1
            r += 1
            
            if s1freq == s2freq:
                return True
        return False