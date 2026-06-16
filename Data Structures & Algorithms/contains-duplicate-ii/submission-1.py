class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic={}
        for ind,val in enumerate(nums):
            if val in dic.keys():
                if abs(ind-dic[val][-1])<=k:
                    return True
                dic[val].append(ind)
            else:
                dic[val]=[ind]
        return False