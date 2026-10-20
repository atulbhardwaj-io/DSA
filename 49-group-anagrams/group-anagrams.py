
from collections import Counter

class Solution(object):
    def groupAnagrams(self, strs):
        result = []
        groups = {}

        for ch in strs:
            key = tuple(sorted(Counter(ch).items()))

            if key in groups:
                result[groups[key]].append(ch)
            else:
                groups[key] = len(result)
                result.append([ch])

        return result


