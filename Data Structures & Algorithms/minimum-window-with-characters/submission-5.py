from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n1 = len(s)
        n2 = len(t)
        left = 0
        dct1 = dict()
        dct2 = dict()
        ans = 0
        have = 0
        need = len(set(t))
        res_len = float('inf')
        res_coords = [-1, -1]
        for i in range(n2):
            if t[i] in dct2:
                dct2[t[i]] += 1
            else:
                dct2[t[i]] = 1
        
        for right in range(n1):
            if s[right] in dct1:
                dct1[s[right]] += 1
            else:
                dct1[s[right]] = 1
            if s[right] in dct2 and dct1[s[right]] == dct2[s[right]]:
                have += 1

            while have == need:
                if len(s[left:right+1]) < res_len:
                    res_len = len(s[left:right+1])
                    res_coords = [left, right]
                dct1[s[left]] -= 1
                if s[left] in dct2 and dct1[s[left]] < dct2[s[left]]:
                    have -= 1
                if dct1[s[left]] == 0:
                    del dct1[s[left]]
                left += 1
                
        return s[res_coords[0]:res_coords[1]+1]
        