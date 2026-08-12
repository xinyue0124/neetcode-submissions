class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        count = Counter() # hashmap char int
        l = 0
        for r, c in enumerate(s):
            count[c] += 1
            while count[c] > 1:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res

