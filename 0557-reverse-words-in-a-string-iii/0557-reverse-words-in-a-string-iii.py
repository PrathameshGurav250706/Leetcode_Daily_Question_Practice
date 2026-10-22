class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        data=s.split()
        for i in range(len(data)):
            data[i]=data[i][::-1]
        a=" ".join(data)
        return a