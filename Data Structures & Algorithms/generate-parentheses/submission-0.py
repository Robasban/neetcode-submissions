class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        pset = {"()"}
        tempset = set()
        s = ""
        for i in range(1, n):
            for p in pset:
                for i in range(len(p)):
                    tempset.add(p[0:i] + "()" + p[i:])
            pset.clear()
            pset = tempset.copy()
            tempset.clear()
        
        return list(pset)