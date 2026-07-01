class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def daystaken(mid):
            ret=0
            curr=0
            for i in weights:
                if curr+i > mid:
                    curr=0
                    ret+=1
                curr+=i
            if curr>0:
                ret+=1
            return ret
        def binary(left,right):
            if left<=right:
                mid=left+(right-left)//2
                d=daystaken(mid)
                if d>days:
                    return binary(mid+1,right)
                else:
                    return binary(left,mid-1)
            return left
        return binary(max(weights),sum(weights))