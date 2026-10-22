class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        data=s.split()
        data.reverse()
        a=" ".join(data)
        return a
        # - Time complexity: O(n), where n is the length of the input string. split processes each character once, reverse touches each word reference once, and join traverses the list of words and their contents to produce the output.

        # - Space complexity: O(n) in the worst case. It creates a list of words (data) that collectively holds all characters, plus the output string built by join. If we consider the output as separate from input, extra space is O(n); otherwise the total auxiliary space is O(n).