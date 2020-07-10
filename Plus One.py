class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        nho =0
        cong = len(digits)*[0]
        cong[0]=1
        digits= digits[::-1]
        print(digits)
        for i in range(len(digits)):
            if digits[i] +nho +cong[i] >=10:
                digits[i] = digits[i]+nho+cong[i]-10
                nho =1
                
            else : 
                digits[i]= digits[i]+nho+cong[i]
                nho =0
                
            
        if nho==1: digits.append(1)
        return digits[::-1]
        