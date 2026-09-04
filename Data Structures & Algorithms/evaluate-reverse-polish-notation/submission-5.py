class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t in "+-*/":
                int2 = int(stack.pop())
                int1 = int(stack.pop())
                if t == "+":
                    stack.append(int1 + int2)
                elif t == "-":
                    stack.append(int1 - int2)
                elif t == "*":
                    stack.append(int1 * int2)
                else:
                    stack.append(int1 / int2)
            else:
                stack.append(t)    
            

        return int(stack[0])