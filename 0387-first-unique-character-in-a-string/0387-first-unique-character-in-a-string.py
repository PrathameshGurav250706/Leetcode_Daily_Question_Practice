class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        # for i in range(len(s)):
        #     if s.count(s[i])==1:
        #         return i
        # return -1

        freq = {}

        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        for i in range(len(s)):
            if freq[s[i]] == 1:
                return i

        return -1
        # Time complexity: O(n) for the first loop to build the frequency map plus O(n) for the second pass to find the first unique character, overall O(n). 
        # Space complexity: O(k) where k is the number of distinct characters in the string (in worst case O(n)
            