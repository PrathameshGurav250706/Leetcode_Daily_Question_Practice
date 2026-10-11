class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        First=int(a,2)
        Second=int(b,2)
        Add=First+Second
        return bin(Add)[2:]
        