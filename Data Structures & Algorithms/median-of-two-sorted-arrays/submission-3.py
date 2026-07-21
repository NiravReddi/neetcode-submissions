class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        tot=len(nums1)+len(nums2)
        if tot%2 ==1 :
            k=(len(nums1)+len(nums2))//2
            r=0
            l=0
            res=0
            i=0
            while(i<=k and r<len(nums1) and l<len(nums2)):
                if nums1[r]<nums2[l]:
                    res=nums1[r]
                    r+=1
                else:
                    res=nums2[l]
                    l+=1
                i+=1
            while (i<=k and r<len(nums1)):
                res=nums1[r]
                r+=1
                i+=1
            while (i<=k and l<len(nums2)):
                res=nums2[l]
                l+=1
                i+=1
            
            return res
        else:
            k=(len(nums1)+len(nums2))//2
            k+=1
            r=0
            l=0
            res1=0
            res2=0
            i=0
            while(i<k and r<len(nums1) and l<len(nums2)):
                if nums1[r]<nums2[l]:
                    res1=res2
                    res2=nums1[r]
                    r+=1
                else:
                    res1=res2
                    res2=nums2[l]
                    l+=1
                i+=1
            while (i<k and r<len(nums1)):
                res1=res2
                res2=nums1[r]
                r+=1
                i+=1
            while (i<k and l<len(nums2)):
                res1=res2
                res2=nums2[l]
                l+=1
                i+=1
            return (res1+res2)/2
        
        
            
        return res