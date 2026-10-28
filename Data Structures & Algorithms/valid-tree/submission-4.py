class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        connect = {i: [] for i in range(n)}
        for p1, p2 in edges:
            connect[p1].append(p2)
            connect[p2].append(p1)

        cycle = set()
        visit = set()

        def dfs(node):
            if node in cycle:
                return False
            if node in visit:
                return True
            cycle.add(node)
            for connected in connect[node]:
                connect[connected].remove(node)
                if not dfs(connected):
                    return False
            visit.add(node)
            cycle.remove(node)
            return True

        for i in range(n):
            if not dfs(i):
                return False
        
        return True