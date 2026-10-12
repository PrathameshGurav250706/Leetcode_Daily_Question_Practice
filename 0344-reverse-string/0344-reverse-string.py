class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        left=0
        right=len(s)-1
        while left<right:
            s[left],s[right]=s[right],s[left]
            left+=1
            right-=1
        # Time complexity: O(n), where n is the length of the string (or list) because each element is swapped once.

        # Space complexity: O(1) extra space, since it performs swaps in place and uses a constant amount of additional variables.
      