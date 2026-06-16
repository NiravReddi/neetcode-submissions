class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res=[]
        dic={"2":'abc','3':'def','4':'ghi','5':'jkl',
                '6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        def dfs(i,st):
            if i>=len(digits) and st!='':
                res.append(st)
                return
            elif i<len(digits):
                for k in dic[digits[i]]:
                    st+=k
                    dfs(i+1,st)
                    st=st[:-1]
        dfs(0,"")
        return res