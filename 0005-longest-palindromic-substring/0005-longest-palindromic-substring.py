class Solution(object):

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        n = len(s)
        start, end = 0, 0

        for i in range(n):

            # Odd length palindrome
            len1 = self.check(s, i, i)

            # Even length palindrome
            len2 = self.check(s, i, i + 1)

            length = max(len1, len2)

            if length > end - start + 1:
                start = i - (length - 1) // 2
                end = i + length // 2

        return s[start:end + 1]


    def check(self, string, left, right):

        while left >= 0 and right < len(string) and string[left] == string[right]:
            left -= 1
            right += 1

        return right - left - 1