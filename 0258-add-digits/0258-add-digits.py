class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
    
        # while len(str(num))>1:
        #     num=sum([int(i) for i in str(num)])
        # return num
       
        while num>=10:
            result=0
            while num>0:

                digit=num%10
                result=result+digit
                num=num//10
            num=result
        return num