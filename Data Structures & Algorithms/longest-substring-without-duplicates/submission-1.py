class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cur = 0
        ans = 0
        n = len(s)
        left = 0
        for right in range(n):
            if len(s[left:right+1]) == len(set(s[left:right+1])):
                ans = max(ans, len(s[left:right+1]))
            else:
                left += 1
        return ans