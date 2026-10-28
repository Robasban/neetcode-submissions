class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}
        for a, b in prerequisites:
            preMap[a].append(b)
        
        visiting = set()

        def dfs(course):
            if course in visiting:
                return False
            if len(preMap[course]) == 0:
                return True

            visiting.add(course)
            for p in preMap[course]:
                if not dfs(p):
                    return False
            visiting.remove(course)
            preMap[course] = []
            return True


        for course in range(numCourses):
            if not dfs(course):
                return False
        return True