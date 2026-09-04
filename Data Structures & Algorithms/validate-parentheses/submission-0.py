class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if len(stack) == 0:
                stack.append(s[i])
            elif (stack[-1] == "(" and s[i] == ")"):
                stack.pop()
            elif (stack[-1] == "[" and s[i] == "]"):
                stack.pop()
            elif (stack[-1] == "{" and s[i] == "}"):
                stack.pop()
            else:
                stack.append(s[i])
        return len(stack) == 0