# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        low =0
        high = n
        num = (low + high)/2
        while(guess(num)!=0):
            if(guess(num)>0):
                low = num + 1
    
            else:
                high = num
    
            num = (low + high)/2
        return num
    
