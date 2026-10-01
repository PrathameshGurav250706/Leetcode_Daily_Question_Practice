class Solution(object):
    def firstPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        for i in words:
            if i==i[::-1]:
                return i
        return ""
        # The function iterates through each word in the input list once. For each word w, it compares w to its reverse w[::-1], which takes O(len(w)) time. In the worst case, if no palindrome exists, it checks all words. Let n be the number of words and m be the maximum length of a word. Time complexity: O(sum(len(w)) over all words) which is O(n * m) in the worst case. Space complexity: O(1) extra space, besides the input, since it uses a constant amount of additional space and the reverse is computed on the fly.