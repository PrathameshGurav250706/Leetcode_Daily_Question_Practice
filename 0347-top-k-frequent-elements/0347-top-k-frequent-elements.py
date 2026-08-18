class Solution(object):
    def topKFrequent(self, nums, k):
        fre = {}

        for num in nums:
            if num in fre:
                fre[num] = fre[num] + 1
            else:
                fre[num] = 1

        high = [val for val in fre.values()]
        high.sort()

        new =set()

        for key in fre:
            for i in range(1, k + 1):
                if fre[key] == high[-i]:
                    new.add(key)

        return list(new)