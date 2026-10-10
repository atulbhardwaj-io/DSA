
class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        ans = []
        word_length = 0
        count = 0
        line_words = []

        for word in words:
            if word_length + len(word) + count > maxWidth:
                need = maxWidth - word_length
                gaps = count - 1

                if gaps == 0:
                    temp = line_words[0] + ' ' * need
                else:
                    spaces_per_gap = need // gaps
                    extra_spaces = need % gaps
                    temp = ""

                    for i in range(count):
                        temp += line_words[i]

                        if i < gaps:
                            if extra_spaces > 0:
                                temp += ' ' * (spaces_per_gap + 1)
                                extra_spaces -= 1
                            else:
                                temp += ' ' * spaces_per_gap

                ans.append(temp)

                # Reset for the next line
                line_words = []
                word_length = 0
                count = 0

            line_words.append(word)
            word_length += len(word)
            count += 1

        # Last line: left-justified
        temp = ' '.join(line_words)
        temp += ' ' * (maxWidth - len(temp))
        ans.append(temp)

        return ans