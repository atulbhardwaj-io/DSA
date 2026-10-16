
class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        last_occurrence = {}
        for index, char in enumerate(s):
            last_occurrence[char] = index

        ans = []
        i = 0
        end = 0
        start = 0

        while i < len(s):
            end = max(end, last_occurrence[s[i]])

            if i == end:
                ans.append(i - start + 1)
                start = i + 1

            i += 1

        return ans
