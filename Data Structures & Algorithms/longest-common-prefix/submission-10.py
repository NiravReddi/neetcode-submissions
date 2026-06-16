class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res=[]
        for ind,i in enumerate(strs[0]):
            chck=i
            for k in range(len(strs)):
                if ind>=len(strs[k]) or strs[k][ind]!=chck:
                    return "".join(res)
            res.append(chck)
        return "".join(res)
            
            