class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        tmp = [len(nums), nums[-1]]
        for idx, num in enumerate(nums):
            if num == target:
                return idx
            if target < num <= tmp[1]:
                tmp = [idx, num]
        return tmp[0]