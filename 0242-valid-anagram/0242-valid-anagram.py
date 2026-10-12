class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        first=sorted(s)
        second=sorted(t)
        if first==second:
            return True
        return False
        