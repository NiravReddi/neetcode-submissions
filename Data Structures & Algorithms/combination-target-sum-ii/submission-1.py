class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        candidates.sort()
        def dfs(i,s):
            nonlocal res
            if i==len(candidates):
                if sum(s)==target:
                    if s not in res:
                        res.append(s[:])
                return
            if sum(s)>target:
                return
            if sum(s)==target:
                if s not in res:
                    res.append(s[:])
                return
            for k in range(i,len(candidates)):
                s.append(candidates[k])
                dfs(k+1,s)
                s.pop()
            return
        dfs(0,list())
        return res