class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        k1=""
        nho=0
        num1 =  num1[::-1]
        num2 =  num2[::-1]
        if len(num1) > len(num2):
            num2 += (len(num1)-len(num2))*"0"
        else :
            num1 += (len(num2)-len(num1))*"0"
    
    
        for i in range(len(num1)):
        
            if int(num1[i])+int(num2[i])+nho >= 10:
            
                k1 += str(int(num1[i])+int(num2[i])+nho-10)
                nho =  1
            # print (num1[i],num2[i],nho,k1,int(num1[i])+int(num2[i])+nho-10)
        
            else :
                k1 += str(int(num1[i])+int(num2[i])+nho)
                nho =0
        if nho==1:
            k1+="1"
        return k1[::-1]