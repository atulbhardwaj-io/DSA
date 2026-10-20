
class Solution(object):
    def groupAnagrams(self, strs):
        result = {}

        for ch in strs:
            key = "".join(sorted(ch))

            if key not in result:
                result[key] = []

            result[key].append(ch)

        return list(result.values())


