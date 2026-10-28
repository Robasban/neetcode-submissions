class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        neighbors = {i: [] for i in range(n)}
        for p1, p2 in edges:
            neighbors[p1].append(p2)
            neighbors[p2].append(p1)

        visited = set()
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for nei in neighbors[node]:
                dfs(nei)
            return

        res = 0

        for i in range(n):
            if i not in visited:
                res += 1
                dfs(i)

        return res


