class Solution:
    def numDecodings(self, s: str) -> int:
        dic={'1':"A",'2':"B",'3':"C",'4':"D",'5':"E",'6':"F",'7':"G",'8':"H",'9':"I",'10':"J",
        '11':"K",'12':"L",'13':"M",'14':"N",'15':"O",'16':"P",'17':"Q",'18':"R",'19':"S",'20':"T",
        '21':"U",'22':"V",'23':"W",'24':"X",'25':"Y",'26':"Z"}

        res=0
        dp={len(s):1}

        def dfs(i):
            if i in dp:
                return dp[i]
            if s[i]=='0':
                return 0
            res= dfs(i+1)
            if i + 1 < len(s) and (
                s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456"
            ):
                res += dfs(i + 2)
            dp[i]=res
            return res
        return dfs(0)
        