class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        nums3=nums2+nums1
        nums3=sorted(nums3)
        length=len(nums3)
        if len(nums3)%2==0:
            return (nums3[length//2]+nums3[(length//2)-1])/2
        else:
            return nums3[length//2]
        
    