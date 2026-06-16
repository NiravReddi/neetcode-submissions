class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dic=defaultdict(list)

        for i in range(len(prerequisites)):
            dic[prerequisites[i][1]].append(prerequisites[i][0])
        
        visiting=set()

        def dfs(crs):
            if crs in visiting:
                return False
            if dic[crs] == []:
                return True

            visiting.add(crs)
            for pre in dic[crs]:
                if not dfs(pre):
                    return False
            visiting.remove(crs)
            dic[crs] = []
            return True
        for c in range(numCourses):
            
            if not dfs(c):
                
                return False
        return True