class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash=defaultdict()
        ind=0
        for i in nums:
            if target-i in hash.keys():
                return [hash[target-i],ind]
            hash[i]=ind
            ind+=1
        