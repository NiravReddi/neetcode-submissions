class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        dic=defaultdict(list)
        j=0
        for i in nums:
            dic[i].append(j)
            j+=1
        r=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if -(nums[i]+nums[j]) in dic.keys():
                    for k in dic[-(nums[i]+nums[j])]:
                        if k!=i and k!=j and sorted([nums[i],nums[j],nums[k]]) not in r:
                            r.append(sorted([nums[i],nums[j],nums[k]]))
                            
        return r
