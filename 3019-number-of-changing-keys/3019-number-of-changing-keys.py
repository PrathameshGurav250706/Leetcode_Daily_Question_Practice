class Solution(object):
    def countKeyChanges(self, s):
        """
        :type s: str
        :rtype: int
        """
        count=0
        for i in range(1,len(s)):
            if s[i].lower()!=s[i-1].lower():
                count+=1
        return count
        # Time complexity: O(n), where n is the length of the string s. The loop runs once for each character after the first.

        # Space complexity: O(1), since only a few constant-size variables are used regardless of input size.
        