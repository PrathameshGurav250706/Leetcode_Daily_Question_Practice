class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s=s.lower()
        a=""
        for i in s:
            if i.isalnum():
                a+=i
        left=0
        right=len(a)-1
        while left<right:
            if a[left]!=a[right]:
                return False
            left+=1
            right-=1
        return True