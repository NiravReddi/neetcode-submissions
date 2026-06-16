class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dic=defaultdict(list)

        for i in range(len(prerequisites)):
            dic[prerequisites[i][1]].append(prerequisites[i][0])
        
        visited=[False]*numCourses

        def dfs(crs):
            if visited[crs]==True:
                return False
            if dic[crs] == []:
                return True

            visited[crs]=True
            for pre in dic[crs]:
                if not dfs(pre):
                    return False
            return True
        for c in range(numCourses):
            visited=[False]*numCourses
            if not dfs(c):
                return False
        return True