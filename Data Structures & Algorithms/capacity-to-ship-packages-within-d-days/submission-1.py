class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def check(mid):
            ret=0
            running=0
            for i in weights:
                if running+i>mid:
                    ret+=1
                    running=0
                running+=i
            if running>0:
                ret+=1
            return ret
        def binary(left,right):
            if left<=right:
                mid=left+(right-left)//2
                if check(mid)>days:
                    return binary(mid+1,right)
                else:
                    return binary(left,mid-1)
            return left
        return binary(max(weights),sum(weights))
        