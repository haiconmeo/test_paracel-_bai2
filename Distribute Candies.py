class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        loai = set(candies)
        return min(len(loai), len(candies)//2)