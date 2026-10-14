class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        text1 = s
        text2 = s[::-1]

        m = len(text1)
        n = len(text2)

        t = [[-1] * (n + 1) for _ in range(m + 1)]

        def LCS(m, n):
            if m == 0 or n == 0:
                return 0

            if t[m][n] != -1:
                return t[m][n]

            if text1[m - 1] == text2[n - 1]:
                t[m][n] = 1 + LCS(m - 1, n - 1)
            else:
                t[m][n] = max(
                    LCS(m, n - 1),
                    LCS(m - 1, n)
                )

            return t[m][n]

        return LCS(m, n)