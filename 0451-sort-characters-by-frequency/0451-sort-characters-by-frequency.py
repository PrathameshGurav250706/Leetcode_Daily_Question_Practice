from collections import Counter

class Solution(object):
    def frequencySort(self, s):
        count1 = Counter(s)
        
        arr = list(count1.values())
        arr.sort(reverse=True)
        
        result = ""
        
        for val in arr:
            for char in count1:
                if val == count1[char]:
                    result += char * val
                    count1[char] = 0
        
        return result