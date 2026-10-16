
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # if not strs:
        #     return ""

        # first = strs[0]

        # for i in range(len(first)):
        #     for s in strs[1:]:
        #         if i >= len(s) or first[i] != s[i]:
        #             return first[:i]

        # return first
        prefix = strs[0]

        for word in strs[1:]:
            while not word.startswith(prefix):
                prefix = prefix[:-1]

                if prefix == "":
                    return ""

        return prefix