class Solution(object):
    def check(self,n):
        s=0
        while n>0:
            s += (n%10)**2
            n//=10
        return s
            
    def isHappy(self, n):
        
        seen = set()
        while n not in seen:
            seen.add(n)
            n = sum(int(num) ** 2 for num in str(n))
        return n == 1