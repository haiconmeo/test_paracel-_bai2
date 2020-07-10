class Solution(object):
    def maxDivide(self, a, b ): 
        while a % b == 0: 
            a = a / b 
        return a 
    def isUgly(self, no):
        """
        :type num: int
        :rtype: bool
        
        """
        if no<1 :
            return False
        if no ==1: return True
        no = self.maxDivide(no, 2) 
        no = self.maxDivide(no, 3) 
        no = self.maxDivide(no, 5) 
        return 1 if no == 1 else 0

    
        