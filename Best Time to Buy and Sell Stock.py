class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        kq = 0
        mua = 1000000
        for price in prices:
            if price < mua:
                mua = price
            if price - mua > kq:
                kq = price - mua
        return kq