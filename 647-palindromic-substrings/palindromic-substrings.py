class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        i = 0
        while i < len(s):
            j = i + 1
            while j < len(s) + 1:
                temp = s[i:j] 
                if temp == temp[::-1]:
                    count += 1
                j += 1 
            i += 1      
        return count
