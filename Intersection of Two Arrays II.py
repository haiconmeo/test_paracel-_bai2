class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dem = dict()
        kq = []
        for num in nums1:
            dem[num] = dem.get(num, 0) + 1
        for num in nums2:
            if dem.get(num, 0):
                kq.append(num)
                dem[num] -= 1
        return kq