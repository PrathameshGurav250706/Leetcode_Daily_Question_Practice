class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        MIN = -2**31
        MAX = 2**31 - 1
        if x>0:
            new=0
            while x>0:
                digit=x%10
                new=new*10+digit
                x=x//10
            if new > MAX:
                return 0

            return new
        else:
            x=abs(x)
            new=0
            while x>0:
                digit=x%10
                new=new*10+digit
                x=x//10
            new=-new

            if new < MIN:
                return 0

            return new
            # Time complexity: O(log10 |x|) because the loop processes one digit per iteration, so it runs proportional to the number of digits in x. In the worst case, for 32-bit integers, that's at most about 10 iterations.

            # Space complexity: O(1) since it uses a constant amount of extra space (a few integer variables) regardless of input size.