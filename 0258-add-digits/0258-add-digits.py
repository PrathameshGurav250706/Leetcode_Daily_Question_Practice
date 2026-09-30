class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        # while num>10:
        #     digit=num%10
        while len(str(num))>1:
            num=sum([int(i) for i in str(num)])
        return num