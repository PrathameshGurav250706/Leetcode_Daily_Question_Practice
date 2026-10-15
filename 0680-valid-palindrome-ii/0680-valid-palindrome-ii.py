class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def check(left,right):
            while left<right:
                if s[left]!=s[right]:
                    return False
                left+=1
                right-=1
            return True
        left=0
        right=len(s)-1
        while left<right:
            if s[left]!=s[right]:
                return check(left+1,right) or check(left,right-1)
            left+=1
            right-=1
        return True
        # Time complexity: O(n), where n is the length of the string. In the worst case, the two-pointer scan traverses the string once, and the inner check may traverse a portion of the string again, but each pair of mismatches is handled at most twice, keeping overall linear.

        # Space complexity: O(1), excluding the input string. The algorithm uses a constant number of extra variables and a small helper function, with no additional data structures.