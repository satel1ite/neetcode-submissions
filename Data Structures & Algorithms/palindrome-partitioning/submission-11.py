class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if s == '':
            return []
        n = len(s)

        def isPalindrome(s: str) -> bool:
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

        res = []
        def backtrack(st, path):
            if st == n:
                res.append(path.copy())
                return
            
            for en in range(st, n):
                if isPalindrome(s[st:en+1]):
                    path.append(s[st:en+1])
                    backtrack(en+1, path)
                    path.pop()

        backtrack(0, [])
        return res