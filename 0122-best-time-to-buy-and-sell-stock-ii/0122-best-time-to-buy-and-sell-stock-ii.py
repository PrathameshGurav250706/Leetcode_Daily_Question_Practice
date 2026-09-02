class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # Time Complexity-O(n)
        # Space Complexity- O(1)

        # Logic is -> profit is max where next price is grater than current price, Add all maxProfit 
        
        maxProfit=0
        for i in range(1,len(prices)):
            if prices[i]>prices[i-1]:
                maxProfit=maxProfit+prices[i]-prices[i-1]
        return maxProfit