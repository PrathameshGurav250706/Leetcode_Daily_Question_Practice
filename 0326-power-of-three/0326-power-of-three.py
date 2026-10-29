class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # p=0
        # while True:
        #     if 3**p==n:
        #         return True
        #     if 3**p>2**31-1:
        #         return False
        #     p+=1
        if n<1:
            return False
        while n%3==0:
            n//=3
        return n==1