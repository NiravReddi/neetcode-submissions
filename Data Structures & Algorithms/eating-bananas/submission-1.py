class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check(mid):
            total=0
            for i in piles:
                total+=math.ceil(float(i)/mid)
            return total
        res=max(piles)
        def binary(left,right):
            nonlocal res
            if left<=right:
                mid=left+(right-left)//2
                
                if check(mid)<=h:
                    res=mid
                    return binary(left,mid-1)
                else:
                    return binary(mid+1,right)
                
            return left
        binary(1,res)
        return res