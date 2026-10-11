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
        

        # i = len(a) - 1
        # j = len(b) - 1
        # carry = 0
        # result = []

        # while i >= 0 or j >= 0 or carry:
        #     total = carry

        #     if i >= 0:
        #         total += int(a[i])
        #         i -= 1

        #     if j >= 0:
        #         total += int(b[j])
        #         j -= 1

        #     result.append(str(total % 2))
        #     carry = total // 2

        # result.reverse()

        # return ''.join(result)