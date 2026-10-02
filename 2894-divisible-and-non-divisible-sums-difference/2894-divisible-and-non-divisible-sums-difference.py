class Solution(object):
    def differenceOfSums(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        a=sum([i for i in range(1,n+1) if i%m!=0])
        b=sum([i for i in range(1,n+1) if i%m==0])
        return a-b

        # a=b=0
        # for i in range(1,n+1):
        #     if i%m!=0:
        #         a+=i
        #     else:
        #         b+=i
        # return a-b