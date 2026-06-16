class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l=0
        dic=defaultdict(int)
        for i in range(len(nums)):
            if nums[i] in dic.keys():
                if abs(dic[nums[i]]-i) <=k:
                    return True
            dic[nums[i]]=i
        return False
        