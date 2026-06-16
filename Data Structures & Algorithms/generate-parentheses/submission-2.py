class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        def dfs(s,o,c):
            nonlocal res
            print(s)
            if o==c==n:
                res.append(s)
            if len(s)>=(n*2):
                return
            if o>c:
                dfs(s+")",o,c+1)
            dfs(s+'(',o+1,c)
        dfs("",0,0)
        return res