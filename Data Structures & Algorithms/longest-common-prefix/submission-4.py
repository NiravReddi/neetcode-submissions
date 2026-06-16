class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res=""
        st=strs[0]
        ind=0
        for ind in range(0,len(st)):
            flag=True
            for i in range(len(strs)):
                if len(strs[i])<=ind or st[ind]!=strs[i][ind]:
                    return res
            if flag:
                res+=st[ind]
        return res
                