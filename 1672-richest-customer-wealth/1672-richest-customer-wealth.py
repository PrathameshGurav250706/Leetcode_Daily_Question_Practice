class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        Max=0
        for i in accounts:
            wealth=sum(i)
            Max=max(Max,wealth)
        return Max