class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l=0
        r=0
        while(l<m and r<len(nums2)):
            if nums2[r]<nums1[l]:
                nums1.insert(l,nums2[r])
                nums1.pop()
                r+=1
                m+=1   
            l+=1
        while(r<len(nums2)):
            nums1[l]=nums2[r]
            l+=1
            r+=1

            
        