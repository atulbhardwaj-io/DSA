
class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        hash = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        ans = []

        if len(digits) == 1:
            return list(hash[digits])

        elif len(digits) == 2:
            for i in range(len(hash[digits[0]])):
                for j in range(len(hash[digits[1]])):
                    temp = hash[digits[0]][i] + hash[digits[1]][j]
                    ans.append(temp)
            return ans

        elif len(digits) == 3:
            for i in range(len(hash[digits[0]])):
                for j in range(len(hash[digits[1]])):
                    for k in range(len(hash[digits[2]])):
                        temp = hash[digits[0]][i] + hash[digits[1]][j] + hash[digits[2]][k]
                        ans.append(temp)
            return ans
        else:
            for i in range(len(hash[digits[0]])):
                for j in range(len(hash[digits[1]])):
                    for k in range(len(hash[digits[2]])):
                        for l in range(len(hash[digits[3]])):
                            temp = hash[digits[0]][i] + hash[digits[1]][j] + hash[digits[2]][k] + hash[digits[3]][l]
                            ans.append(temp)
            return ans
