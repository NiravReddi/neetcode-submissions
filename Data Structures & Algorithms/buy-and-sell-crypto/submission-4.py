class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        lmin=prices[0]
        res=0
        while(l<len(prices)):
            if lmin>prices[l]:
                lmin=prices[l]

            res=max(res,prices[l]-lmin)
            l+=1
        return res

        