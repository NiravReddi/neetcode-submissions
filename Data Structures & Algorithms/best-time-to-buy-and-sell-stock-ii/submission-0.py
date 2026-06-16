class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dic=defaultdict(int)

        def dfs(i,prev):
            nonlocal dic
            if i>=len(prices):
                return 0
            if (i,prev) in dic.keys():
                return dic[(i,prev)]
            else:
                if prev!=-1:
                    sell=prices[i]-prev+dfs(i+1,-1)
                    notsell=dfs(i+1,prev)
                    dic[(i,prev)]=max(sell,notsell)
                    return dic[(i,prev)]
                dic[(i,prev)]=max(dfs(i+1,prices[i]),dfs(i+1,-1))
                return dic[(i,prev)]
        return dfs(0,-1)
