class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = {i: [] for i in range(numCourses)}

        for c, p in prerequisites:
            prereq[c].append(p)
        
        res = []

        visiting = set()
        visited = set()

        def dfs(crs):
            if crs in visiting:
                return False
            if crs in visited:
                return True
            
            visiting.add(crs)
            for p in prereq[crs]:
                if not dfs(p):
                    return False
            res.append(crs)
            visited.add(crs)
            visiting.remove(crs)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []

        return res        



