
class Solution(object):
    def strStr(self, haystack, needle):
        n = len(needle)

        for i in range(len(haystack) - n + 1):
            if haystack[i:i+n] == needle:
                return i

        return -1
        # Time complexity: O(mn) in the worst case, where m is the length of haystack and n is the length of needle. For each of the m−n+1 starting positions, the substring comparison can scan up to n characters.

        # Space complexity: O(1) extra space (excluding the input), since it uses a constant number of variables and only stores lengths and an index.