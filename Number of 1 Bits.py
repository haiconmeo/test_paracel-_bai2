class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        print(n)
        kq=0
        n = str(bin(n))
        print (n)
        for i in n:
            print(i)
            if i =='1':
                kq+=1
        return kq
        