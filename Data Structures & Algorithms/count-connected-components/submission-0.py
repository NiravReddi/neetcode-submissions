class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited=set()
        dic=defaultdict(list)
        for i in edges:
            dic[i[0]].append(i[1])
            dic[i[1]].append(i[0])
        def dfs(i,prev):
            if i in visited:
                return 
            visited.add(i)

            for j in dic[i]:
                if j == prev:
                    continue
                dfs(j,i)
        prevvisited=0
        r=0
        for i in range(n):
            dfs(i,-1)
            if len(visited)==n:
                return r+1
            else:
                if len(visited)>prevvisited:
                    r+=1
                prevvisited=len(visited)
        return r
            
        


        