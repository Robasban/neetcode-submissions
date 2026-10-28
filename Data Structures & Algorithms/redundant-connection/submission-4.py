class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        neighbors = {i: [] for i in range(1, len(edges) + 1)}
        for p1, p2 in edges:
            neighbors[p1].append(p2)
            neighbors[p2].append(p1)

        cycle = set()

        def dfs(node, parent, start):
            if node in cycle:
                return node == start
            cycle.add(node)
            for nei in neighbors[node]:
                if nei == parent:
                    continue
                if dfs(nei, node, start):
                    return True
            cycle.remove(node)
            return False
        
        for i in range(1, len(edges) + 1):
            if dfs(i, -1, i):
                break
        
        for i in range(len(edges) - 1, -1, -1):
            if edges[i][0] in cycle and edges[i][1] in cycle:
                return edges[i]