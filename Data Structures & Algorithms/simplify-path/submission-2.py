class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        path2 = ''

        for i in range(len(path)):
            if len(path2) > 0 and path2[-1] == '/' and path[i] == '/':
                continue
            else:
                path2 += path[i]

        stack = []

        path2 = path2.split('/')

        for s in path2:
            if s == '' or s == '.':
                continue
            
            if s == '..':
                if stack:
                    stack.pop()
            
            else:
                stack.append(s)

        res = '/'.join(stack)
        if len(res) > 0 and res[0] != '/':
            res = '/' + res
        if len(res) == 0:
            res = '/' + res
        
        if len(res) > 1 and res[-1] == '/':
            res = res[:-1]

        return res