class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        cur = 0
        ans = 0
        n = len(s)
        left = 0
        dct = dict()
        for right in range(n):
            if s[right] in dct:
                dct[s[right]] += 1
            else:
                dct[s[right]] = 1
            if right - left + 1 - max(dct.values()) <= k:
                ans = max(ans, right - left + 1)
            else:
                while right - left + 1 - max(dct.values()) > k:
                    dct[s[left]] -= 1
                    left += 1
                ans = max(ans, right - left + 1)

        return ans