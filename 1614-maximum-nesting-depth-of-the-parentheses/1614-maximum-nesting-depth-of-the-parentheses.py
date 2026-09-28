class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        curr=0
        Max=0
        for i in s:
            if i=='(':
                curr+=1
            if i==')':
                Max=max(Max,curr)
                curr-=1
        return Max


        