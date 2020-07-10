class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tong=0
        maxx =  len(nums)
        for i in range(maxx+1):
            tong+=i
        return tong- sum(nums)
        