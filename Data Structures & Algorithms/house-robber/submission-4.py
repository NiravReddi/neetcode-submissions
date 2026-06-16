class Solution:
    def rob(self, nums: List[int]) -> int:
        dic=defaultdict(int)
        def fun(i):
            if i==len(nums)-1:
                return nums[i]
            if i==len(nums)-2:
                return nums[i]
            if i>=len(nums):
                return 0
            if i in dic.keys():
                return nums[i]+dic[i]
            mx=max(fun(i+2),fun(i+3))
            dic[i]=max(dic[i],mx) 
            return nums[i]+dic[i]
        
        return max(fun(0),fun(1))
        