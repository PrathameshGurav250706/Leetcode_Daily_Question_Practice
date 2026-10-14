class Solution(object):
    def maxSumOfSquares(self, num, sum):
        """
        :type num: int
        :type sum: int
        :rtype: str
        """
        if sum>9*num:
            return ""
        result=[]

        for i in range(num):
            digit=min(9,sum)
            result.append(str(digit))
            sum-=digit
        if sum>0:
            return ""

        return ''.join(result)
        # - Time complexity: O(num) because the for loop iterates exactly num times, performing O(1) work per iteration.

        # - Space complexity: O(num) for storing the resulting digits in the list result, which is then joined into a string.
