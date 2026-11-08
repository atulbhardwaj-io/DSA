class Solution:
    def frequencySort(self, s: str) -> str:
        counter = {}
        ans = ""
        for ch in list(s):
            counter[ch] = counter.get(ch, 0)+1
        sorted_item = sorted(counter.items(), key=lambda x: x[1], reverse = True)
        for key,value in sorted_item:
            ans += key*value
        return ans