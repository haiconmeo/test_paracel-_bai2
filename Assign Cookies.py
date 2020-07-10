class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        g_len = len(g)-1
        c = 0
        for i in s:
            if c > g_len:
                break
            if i >= g[c]:
                c += 1
        return c