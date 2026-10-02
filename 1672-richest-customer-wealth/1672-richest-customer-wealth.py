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
        # Time complexity: O(mn) where m is the number of customers (rows) and n is the number of banks (columns). Each account row is summed once.

        # Space complexity: O(1) extra space, aside from the input. Uses a constant amount of additional variables (Max and wealth).