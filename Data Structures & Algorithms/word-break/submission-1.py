class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dic={}
        def dfs(string):
            if string in dic.keys():
                return dic[string]
            if string=="":
                return True
            for i in wordDict:
                if string.startswith(i):
                    dic[string[len(i):]]=dfs(string[len(i):])
                    if dic[string[len(i):]]:
                        return True
            return False
        return dfs(s)
            
        