class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        Max=0
        for i in accounts:
            Max=max(Max,sum(i))
        return Max