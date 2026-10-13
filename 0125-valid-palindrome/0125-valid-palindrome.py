class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s=s.lower()
        new=""
        for i in s:
            if i.isalnum():
                new+=i

        left=0
        right=len(new)-1
        while left<right:
            if new[left]!=new[right]:
                return False
            left+=1
            right-=1
        return True
#         Time complexity:
# - Converting to lowercase: O(n) where n is the input length.
# - Building new string by filtering alphanumeric: O(n).
# - Palindrome check with two pointers on the filtered string of length m (m <= n): O(m).
# Overall, O(n) time in the worst case.

# Space complexity:
# - new stores the filtered string of length m (worst-case m = n). Additional O(1) extra beyond the output string.
# Total auxiliary space: O(n) for the filtered string; if counting input/output separately, the auxiliary space is O(n)

        