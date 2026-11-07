class Solution(object):
    def commonChars(self, words):
        ans = []
        first_li = list(words[0])

        for ch in first_li:
            found = True

            for i in range(1, len(words)):
                if ch not in words[i]:
                    found = False
                    break

            if found:
                ans.append(ch)

                # Remove this occurrence so it cannot be reused
                for i in range(1, len(words)):
                    words[i] = words[i].replace(ch, '', 1)

        return ans
 