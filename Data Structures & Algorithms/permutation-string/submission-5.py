class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dct1 = dict()
        dct2 = dict()
        n1 = len(s1)
        n2 = len(s2)
        
        for i in range(n1):
            if s1[i] in dct1:
                dct1[s1[i]] += 1
            else:
                dct1[s1[i]] = 1 

        left = 0
        for right in range(n2):
            if s2[right] in dct2:
                dct2[s2[right]] += 1
            else:
                dct2[s2[right]] = 1
            

            if right - left + 1 > n1:
                dct2[s2[left]] -= 1
                if dct2[s2[left]] == 0:
                    del dct2[s2[left]]
                left += 1
            if dct1 == dct2:
                return True
        return False
            