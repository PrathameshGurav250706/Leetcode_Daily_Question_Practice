class Solution(object):
    def findWordsContaining(self, words, x):
        """
        :type words: List[str]
        :type x: str
        :rtype: List[int]
        """
        new=[]
        for i in range(len(words)):
            if x in words[i]:
                new.append(i)
        return new
        # Time complexity:
        # - For each of n words, it checks whether substring x is contained in the word, which in the worst case costs O(m) time for a word of length m. Overall, the time is O(sum length of words) in the worst case, which is O(n * L) if we denote average word length by L. In typical terms, it's O(n * k) where k is average length of a word.

        # Space complexity:
        # - It stores the indices of matching words in a new list. In the worst case, all words match, so the extra space is O(n). Other than the output list, the function uses O(1) additional space.