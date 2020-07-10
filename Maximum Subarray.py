class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxSum = leftSum = -99999999999
        for num in nums:
            leftSum = max(num, leftSum + num)
            maxSum = max(leftSum, maxSum)
        return maxSum