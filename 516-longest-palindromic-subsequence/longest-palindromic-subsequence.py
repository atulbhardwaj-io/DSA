
class Solution(object):
    def longestPalindromeSubseq(self, s):
        l = len(s)
        first = 0
        last = l - 1

        t = [[-1] * l for _ in range(l)]

        def lps(first, last):
            if first > last:
                return 0

            if first == last:
                return 1

            if t[first][last] != -1:
                return t[first][last]

            if s[first] == s[last]:
                t[first][last] = 2 + lps(first + 1, last - 1)
            else:
                t[first][last] = max(
                    lps(first + 1, last),
                    lps(first, last - 1)
                )

            return t[first][last]

        return lps(first, last)