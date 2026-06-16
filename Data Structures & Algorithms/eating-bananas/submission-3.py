class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check(mid):
            ret=0
            for i in piles:
                ret+=math.ceil(i/mid)
                
            return ret
        def binary(left,right):
            if left<=right:
                mid=left+(right-left)//2
                
                if check(mid)>h:
                    return binary(mid+1,right)
                else:
                    return binary(left,mid-1)
            return left
        return binary(1,max(piles))