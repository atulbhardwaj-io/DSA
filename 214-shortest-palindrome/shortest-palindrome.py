class Solution:
    def computeLPS(self, pattern, lps):
        M = len(pattern)
        length = 0

        lps[0] = 0
        i = 1

        while i < M:
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1

    def shortestPalindrome(self, s):
        rev = s[::-1]

        temp = s + "-" + rev

        LPS = [0] * len(temp)
        self.computeLPS(temp, LPS)

        longestLPSLength = LPS[len(temp) - 1]

        culprit = rev[:len(s) - longestLPSLength]

        return culprit + s


sol = Solution()

s = "aacecaaa"
print(sol.shortestPalindrome(s))