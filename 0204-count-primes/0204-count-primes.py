class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # count=0
        # if n<2:
        #     return 0
        # for i in range(2,n):
        #     prime=True
        #     for j in range(2, int(i ** 0.5) + 1):
        #         if i%j==0:
        #             prime=False
        #             break
        #     if prime:
        #         count+=1
        # return count
        if n<2:
            return 0
        
        data=[True]*n
        data[0]=data[1]=False
        for i in range(2,int(n**0.5)+1):
            if data[i]:
                for j in range(i*i,n,i):
                    data[j]=False
        return sum(data)