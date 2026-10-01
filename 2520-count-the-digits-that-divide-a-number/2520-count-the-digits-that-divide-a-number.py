class Solution(object):
    def countDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        count=0
        for i in str(num):
            if num%int(i)==0:
                count+=1
        return count
        # Time complexity: O(d) where d is the number of digits in num, since it iterates over each digit once and does O(1) work per digit.

        # Space complexity: O(1) aside from the input representation, since it uses a constant amount of extra space (a few integers) and does not allocate space proportional to num.