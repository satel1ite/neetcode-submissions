class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        dct = dict()
        dct[2] = ['a', 'b', 'c']
        dct[3] = ['d', 'e', 'f']
        dct[4] = ['g', 'h', 'i']
        dct[5] = ['j', 'k', 'l']
        dct[6] = ['m', 'n', 'o']
        dct[7] = ['p', 'q', 'r', 's']
        dct[8] = ['t', 'u', 'v']
        dct[9] = ['w', 'x', 'y', 'z']

        res = []
        def backtrack(i, path):
            if i == len(digits):
                res.append(path)
                return
            letters = dct[int(digits[i])]
            for char in letters:
                backtrack(i + 1, path + char)
        backtrack(0, '')
        return res