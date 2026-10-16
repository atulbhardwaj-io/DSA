
class Solution(object):
    def smallestSubsequence(self, s):
        li = list(s)
        ans = []
        d = {}
        for index, char in enumerate(li):
            d[char] = index
        for index, char in enumerate(li):
            if char not in ans:
                while ans and char < ans[-1] and d[ans[-1]] > index:
                    ans.pop()
                
    
                ans.append(char)
        return "".join(ans)