class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        Prd=1
        Sum=0
        while n>0:
            digit=n%10
            Prd*=digit
            Sum+=digit
            n=n//10
        return Prd-Sum
        