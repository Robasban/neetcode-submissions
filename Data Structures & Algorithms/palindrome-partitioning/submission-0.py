class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        res = []
        subset = []

        def backtrack(lastPart, part):
            if part == len(s):
                if s[lastPart:part] == s[lastPart:part][::-1]:
                    subset.append(s[lastPart:part])
                    res.append(subset.copy())
                    subset.pop()
                return
            
            # partition case
            if s[lastPart:part] == s[lastPart:part][::-1]:
                subset.append(s[lastPart:part])
                backtrack(part, part + 1)
                subset.pop()
            backtrack(lastPart, part + 1)


        backtrack(0, 1)
        
        return res