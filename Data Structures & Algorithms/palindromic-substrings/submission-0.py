class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        for i in range(0, len(s)):
            res += 1
            middle = s[i]
            left = i - 1
            right = i + 1
            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    res += 1
                    left -= 1
                    right += 1
                else:
                    break
            if i != len(s) - 1 and middle == s[i + 1]:
                res += 1
                left = i - 1
                right = i + 2
                while left >= 0 and right < len(s):
                    if s[left] == s[right]:
                        res += 1
                        left -= 1
                        right += 1
                    else:
                        break

        return res