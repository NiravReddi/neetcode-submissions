class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l=0
        r=0
        while(l<m and r<n):
            if nums1[l]<=nums2[r]:
                l+=1
            else:
                
                nums1.insert(l,nums2[r])
                nums1.pop()
                r+=1
                m+=1
        while(r<n):
            nums1[l]=nums2[r]
            l+=1
            r+=1
        
        
        