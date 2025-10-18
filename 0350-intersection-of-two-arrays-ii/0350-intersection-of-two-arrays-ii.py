class Solution(object):
    def intersect(self, nums1, nums2):
        if len(nums1)>len(nums2):
            nums1, nums2= nums2, nums1

        counts = Counter(nums1)
        result=[]
        for num in nums2:
            if counts.get(num,0)>0:
                result.append(num)
            counts[num]-=1
        return result 