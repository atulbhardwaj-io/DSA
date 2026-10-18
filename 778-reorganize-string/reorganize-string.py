class Solution(object):
    def reorganizeString(self, s):
        n = len(s)

        count = [0] * 26
        maxFreq = 0
        maxFreqCh = ''

        for ch in s:
            count[ord(ch) - ord('a')] += 1

            if count[ord(ch) - ord('a')] > maxFreq:
                maxFreq = count[ord(ch) - ord('a')]
                maxFreqCh = ch

            if count[ord(ch) - ord('a')] > (n + 1) // 2:
                return ""

        result = list(s)
        index = 0

        # Place the most frequent character first
        while count[ord(maxFreqCh) - ord('a')] != 0:
            result[index] = maxFreqCh
            index += 2
            count[ord(maxFreqCh) - ord('a')] -= 1

        # Place the remaining characters
        for i in range(26):
            ch = chr(i + ord('a'))

            while count[i] > 0:
                if index >= n:
                    index = 1

                result[index] = ch
                index += 2
                count[i] -= 1

        return "".join(result)

