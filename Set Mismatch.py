class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums=sorted(nums)
        dem = dict()
        for i in range(1,len(nums)+1):
            dem[i]=0
        for i in nums:
            dem[i]+=1
        return [x for x in dem if dem[x]>1]+ [x for x in dem if dem[x]<1]