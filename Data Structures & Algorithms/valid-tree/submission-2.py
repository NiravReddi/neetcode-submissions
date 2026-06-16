class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        dic=defaultdict(list)

        for i in edges:
            dic[i[1]].append(i[0])
            dic[i[0]].append(i[1])
        
        def dfs(i,prev):
            if visited[i]==True:
                return False
            visited[i]=True
            for c in dic[i]:
                if c==prev:
                    continue
                if not dfs(c,i):
                    return False
            return True
        visited=[False]*n
        return dfs(0,-1) and visited.count(True)==n
        