class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        lst = [i for i in s if i in 'abcdefghijklmnopqrstuvwxyz0123456789']
        s = ''.join(lst)
        n = len(s)
        left = 0
        right = n - 1
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return False
        return True