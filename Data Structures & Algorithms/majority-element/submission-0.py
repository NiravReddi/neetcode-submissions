class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mid=len(nums)//2
        dic=defaultdict(int)
        for i in nums:
            dic[i]+=1
            if dic[i]>mid:
                return i
        
        