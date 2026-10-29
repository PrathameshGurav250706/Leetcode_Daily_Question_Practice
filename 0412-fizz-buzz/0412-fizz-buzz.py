class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        data=[0]*n
        for i in range(1,n+1):
            if i%3==0 and i%5!=0:
                data[i-1]="Fizz"
            elif i%5==0 and i%3!=0:
                data[i-1]="Buzz"
            elif i%3==0 and i%5==0:
                data[i-1]="FizzBuzz"
            else:
                data[i-1]=str(i)
        return data