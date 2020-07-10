class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        kq=False
        for i, c in enumerate(s):
            if c == 'A':
                if kq:
                    return False
                kq=True
            if i>1 and c=='L' and s[i-1]=='L' and s[i-2]=='L':
                return False
        return True