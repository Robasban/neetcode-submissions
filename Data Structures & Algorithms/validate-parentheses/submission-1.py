class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            stack.append(s[i])
            if len(stack) > 1:
                if (stack[-2] + stack[-1]) in ["()", "[]", "{}"]:
                    stack.pop()
                    stack.pop()

        return len(stack) == 0