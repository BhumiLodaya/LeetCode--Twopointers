class Solution(object):
    def intersection(self, nums1, nums2):
        set1=set(nums1)
        set2=set(nums2)

        intersection_set=set1.intersection(set2)
        return list(intersection_set)