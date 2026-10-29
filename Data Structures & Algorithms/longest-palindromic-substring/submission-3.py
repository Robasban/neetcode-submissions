class Solution:
    def longestPalindrome(self, s: str) -> str:
        resLen = 1
        res = s[0]

        for i in range(0, len(s) - 1):
            middle = s[i]
            left = i - 1
            right = i + 1
            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    if right - left + 1 > resLen:
                        resLen = right - left + 1
                        res = s[left : right + 1]
                    left -= 1
                    right += 1
                else:
                    break
            if middle == s[i + 1]:
                if resLen == 1:
                    resLen = 2
                    res = s[i : i + 2]
                left = i - 1
                right = i + 2
                while left >= 0 and right < len(s):
                    if s[left] == s[right]:
                        if right - left + 1 > resLen:
                            resLen = right - left + 1
                            res = s[left : right + 1]
                        left -= 1
                        right += 1
                    else:
                        break

        return res