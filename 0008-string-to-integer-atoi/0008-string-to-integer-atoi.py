class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()

        if not s:
            return 0

        sign = 1
        i = 0

        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            i += 1

        result = 0

        while i < len(s) and s[i].isdigit():
            result = result * 10 + int(s[i])
            i += 1

        result = result * sign
        if result < -2**31:
            return -2**31
        if result > 2**31 - 1:
            return 2**31 - 1
        return result
        