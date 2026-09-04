class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t in "+-*/":
                try:
                    int1 = int(stack[-2])
                    int2 = int(stack[-1])
                except:
                    continue
                stack.pop()
                stack.pop()
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