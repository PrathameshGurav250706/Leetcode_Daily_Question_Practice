class Solution(object):
    def scoreOfParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        depth=0
        score=0
        for i in range(len(s)):
            if s[i]=="(":
                depth+=1
            else:
                depth-=1
                if s[i-1]=="(":
                    score+=2**depth
        return score
        # Time: O(n)
        # Space: O(1)