class Solution(object):
    
        
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        trai, phai = 0, len(numbers)-1
        while trai < phai:
            check = numbers[trai] + numbers[phai]
            if check == target:
                return trai+1, phai+1
            if check < target:
                trai += 1
            else:
                phai -= 1