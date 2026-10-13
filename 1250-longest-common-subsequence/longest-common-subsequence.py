class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
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