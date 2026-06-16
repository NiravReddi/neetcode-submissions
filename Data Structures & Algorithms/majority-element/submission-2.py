class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic={}
        mid=len(nums)//2
        for i in nums:
            if i in dic.keys():
                dic[i]+=1
                if dic[i]>mid:
                    return i
            else:
                dic[i]=1
                if dic[i]>mid:
                    return i
