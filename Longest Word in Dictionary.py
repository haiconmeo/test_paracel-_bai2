class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        kq = ""
        wordset = set(words)
        for word in words:
            if len(word) > len(kq) or len(word) == len(kq) and word < kq:
                if all(word[:k] in wordset for k in range(1, len(word))):
                    kq = word

        return kq
        