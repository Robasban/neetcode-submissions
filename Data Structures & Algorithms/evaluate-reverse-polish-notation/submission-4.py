class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t in "+-*/":
                int2 = stack.pop()
                int1 = stack.pop()
                if t == "+":
                    stack.append(int1 + int2)
                elif t == "-":
                    stack.append(int1 - int2)
                elif t == "*":
                    stack.append(int1 * int2)
                else:
                    stack.append(int1 / int2)
            else:
                stack.append(int(t))    
            

        return stack[0]