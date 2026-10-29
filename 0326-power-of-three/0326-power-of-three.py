class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        p=0
        while True:
            if 3**p==n:
                return True
            if 3**p>2**31-1:
                return False
            p+=1