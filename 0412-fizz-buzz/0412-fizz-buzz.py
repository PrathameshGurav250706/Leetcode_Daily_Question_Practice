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
        # Time complexity: O(n). The loop iterates from 1 to n, performing a constant amount of work for each iteration (a few modulo operations and string assignments).

        # Space complexity: O(n). The output list data stores n strings, one for each i, so the auxiliary space grows linearly with n. Additional fixed-space variables are constant.