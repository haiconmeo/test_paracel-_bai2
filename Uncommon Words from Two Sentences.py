class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        count = {}
        kq=[]
        for i in A.split():
            count[i] =  count.get(i,0)+1
        for i in B.split():
            count[i] =  count.get(i,0)+1
        for i in count:
            if count[i] == 1:
                kq.append(i)
        return kq