class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_mul=[]
        suffix_mul=[]
        prefix=1
        suffix=1
        count0=0
        for i in range(len(nums)):
            prefix_mul.append(prefix)
            suffix_mul.insert(0,suffix)
            suffix*=nums[len(nums)-i-1]
            prefix*=nums[i]
            if nums[i]==0:
                count0+=1
                if count0>1:
                    return [0]* len(nums)
        res=[]
        for i in range(len(nums)):
            res.append(prefix_mul[i]*suffix_mul[i])
        return res

        