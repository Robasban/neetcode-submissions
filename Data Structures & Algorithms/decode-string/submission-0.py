class Solution:
    def decodeString(self, s: str) -> str:

        stack = []

        for i in s:
            if i == ']':
                repeat = ''
                count = ''

                while stack and stack[-1] != '[':
                    repeat = stack.pop() + repeat
                
                stack.pop()

                while stack and stack[-1].isdigit():
                    count = stack.pop() + count
                
                count = int(count)

                for _ in range(count):
                    stack.append(repeat)

            
            else:
                stack.append(i)
        
        return ''.join(stack)