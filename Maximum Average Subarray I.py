class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        
        S = 0
        for i in range(k):
            S+=nums[i]
        kq =S
        for i in range(k,len(nums)):
            S+=nums[i]-nums[i-k]
            if S>kq:
                kq = S
        return kq/float(k)