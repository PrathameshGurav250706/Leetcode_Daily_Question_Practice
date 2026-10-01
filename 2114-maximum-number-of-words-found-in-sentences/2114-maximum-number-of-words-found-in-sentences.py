class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        Max=0
        for i in sentences:
            data=i.split(" ")
            Max=max(Max,len(data))
        return Max
        