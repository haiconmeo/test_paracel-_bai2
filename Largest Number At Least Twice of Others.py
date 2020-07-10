class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m =  max(nums)
        if all( m>=2*k for k in nums if k!=m):
            return nums.index(m)
        return -1