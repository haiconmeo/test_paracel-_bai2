class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dem=1
        leng = 1
        if len(nums)==0:
            return 0
        for i in range(len(nums)-1):
            if leng <dem:
                    leng = dem
            if nums[i]<nums[i+1]:
                dem+=1
            else :
                
                dem=1
        if leng <dem:
            leng = dem
        return leng