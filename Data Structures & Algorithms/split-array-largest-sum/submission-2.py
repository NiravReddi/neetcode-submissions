class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def check(mid):
            no_of_division=0
            curr_sum=0
            for i in nums:
                if i+curr_sum>mid:
                    no_of_division+=1
                    curr_sum=i
                else:
                    curr_sum+=i
            if curr_sum>0:
                no_of_division+=1
            return no_of_division
        res=0
        def binary(left,right):
            nonlocal res
            if left<=right:
                mid=left+(right-left)//2
                if check(mid)<=k:
                    res=mid
                    return binary(left,mid-1)
                else:
                    return binary(mid+1,right)
        binary(max(nums),sum(nums))
        return res
