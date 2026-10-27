class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == '':
            return []

        res = []

        mappings = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']

        def bt(index, curr):
            if index == len(digits):
                res.append(''.join(curr))
                return
            
            for char in mappings[int(digits[index]) - 2]:
                curr.append(char)
                bt(index + 1, curr)
                curr.pop()


        bt(0, [])

        return res
