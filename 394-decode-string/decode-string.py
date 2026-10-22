class Solution(object):
    def decodeString(self, s):
        stack = []
        i = 0
        ans = ""
        number = 0

        while i < len(s):
            if s[i].isdigit():
                number = number * 10 + int(s[i])

            elif s[i] == '[':
                stack.append(number)
                stack.append('[')
                number = 0

            elif s[i] == ']':
                stri = ""

                while stack and stack[-1] != '[':
                    stri = stack.pop() + stri

                stack.pop()  # Remove '['

                repeat = stack.pop()  # Get repetition count
                decoded = stri * repeat

                if stack and isinstance(stack[-1], str) and stack[-1] != '[':
                    stack.append(decoded)
                else:
                    stack.append(decoded)

            else:
                stack.append(s[i])

            i += 1

        ans = ""
        for item in stack:
            ans += str(item)

        return ans