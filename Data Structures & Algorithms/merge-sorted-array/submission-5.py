class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        num1copy=nums1[:]
        i=0
        j=0
        k=0
        while(i<m and j<n):
            if num1copy[i]<=nums2[j]:
                nums1[k]=num1copy[i]
                i+=1
            else:
                nums1[k]=nums2[j]
                j+=1
            k+=1
        while(i<m):
            nums1[k]=num1copy[i]
            i+=1
            k+=1
        while(j<n):
            nums1[k]=nums2[j]
            j+=1
            k+=1
        
        