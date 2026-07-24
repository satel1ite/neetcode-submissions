class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = dict()
        for let in s:
            if let in count:
                count[let] += 1
            else:
                count[let] = 1
        for let in t:
            if let in count:
                count[let] -= 1
            else:
                return False
        if len({n for n in count.values() if n != 0}) != 0:
            return False
        else:
            return True 