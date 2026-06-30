class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def consume(mid):
            res=0
            for i in piles:
                res+=math.ceil(i/mid)
            return res
        def binary(left,right):
            if left<=right:
                mid=left+(right-left)//2
                hours=consume(mid)
                if hours>h:
                    return binary(mid+1,right)
                else:
                    return binary(left,mid-1)
            return left
        return binary(1,max(piles))