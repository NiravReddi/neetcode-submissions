class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res=0
        lmin=prices[0]
        for r in range(1,len(prices)):
            lmin=min(prices[r],lmin)
            if lmin<prices[r]:
                res=max(res,prices[r]-lmin)
        return res