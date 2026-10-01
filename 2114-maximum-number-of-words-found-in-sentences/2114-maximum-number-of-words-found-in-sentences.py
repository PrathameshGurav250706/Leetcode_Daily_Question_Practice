class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        Max=0
        for i in sentences:
            data=i.split(" ")
            Max=max(Max,len(data))
        return Max

        # Time complexity: O(N + M) where N is the number of sentences and M is the total number of words across all sentences. For each sentence, it splits into words (cost proportional to the number of words in that sentence) and compares lengths. Overall this sums to the total number of words.

        # Space complexity: O(W) where W is the maximum number of words in a single sentence at any time (due to the temporary list created by split for each sentence). Additional O(1) extra space beyond that.