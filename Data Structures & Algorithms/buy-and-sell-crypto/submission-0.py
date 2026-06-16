class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mx=0
        mn=101
        for right in range(len(prices)):
            print(mn-prices[right],mx)
            if right!=0:
                mx=max(prices[right]-mn,mx)
            mn=min(mn,prices[right])
            
        print("---",mn,mx)    
        return mx
        