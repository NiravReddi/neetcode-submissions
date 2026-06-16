class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def check(mid):
            no_of_days=0
            curr_weight=0
            for i in weights:
                if i+curr_weight >mid:
                    no_of_days+=1
                    curr_weight=i
                else:
                    curr_weight+=i
            if curr_weight>0:
                no_of_days+=1
            return no_of_days
        res=sum(weights)
        def binary(left,right):
            nonlocal res
            if left<=right:
                mid=left+(right-left)//2
                if check(mid)<=days:
                    res=mid
                    return binary(left,mid-1)
                else:
                    return binary(mid+1,right)
        binary(max(weights),res)
        return res