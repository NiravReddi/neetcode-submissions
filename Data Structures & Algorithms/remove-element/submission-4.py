class Solution:
    def removeElement(self, nums: List[int], vals: int) -> int:
        dic=[]
        for ind,val in enumerate(nums):
            if val==vals:
                dic.append(ind)
        res=0
        while(res<len(dic)):
            nums.pop(dic[res]-res)
            res+=1
        return len(nums)
        