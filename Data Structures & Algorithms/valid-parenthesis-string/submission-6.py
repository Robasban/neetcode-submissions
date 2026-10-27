class Solution:
    def checkValidString(self, s: str) -> bool:
        leftStack = []
        starStack = []

        for i, c in enumerate(s):
            if c == "(":
                leftStack.append(i)
            elif c == "*":
                starStack.append(i)
            else:
                if leftStack:
                    leftStack.pop()
                elif starStack:
                    starStack.pop()
                else:
                    return False
        
        while leftStack:
            if not starStack:
                return False
            if starStack[-1] < leftStack[-1]:
                return False
            else:
                leftStack.pop()
                starStack.pop()
        
        return True