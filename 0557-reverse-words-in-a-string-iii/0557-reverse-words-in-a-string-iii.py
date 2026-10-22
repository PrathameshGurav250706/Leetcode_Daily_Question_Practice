class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # data=s.split()
        # for i in range(len(data)):
        #     data[i]=data[i][::-1]
        # a=" ".join(data)
        # return a
        #  time complexity is O(n). Space usage is O(n) to store the list of words and the final string.

        return " ".join([word[::-1] for word in s.split(" ")])