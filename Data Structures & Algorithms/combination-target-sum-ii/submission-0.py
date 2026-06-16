class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        candidates.sort()

        def dfs(i,s):
            if sum(s)==target:
                if s not in res:
                    res.append(s)
                return
            elif sum(s)>target or i>=len(candidates):
                return
            dfs(i+1,s)
            dfs(i+1,s+[candidates[i]])
        dfs(0,[])
        return res