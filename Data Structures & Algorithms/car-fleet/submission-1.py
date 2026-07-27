class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ans = 0
        stack = []
        lst = []
        n = len(speed)
        for i in range(n):
            sp = speed[i]
            pos = position[i]
            lst.append([pos, sp])
        lst.sort(key=lambda x: x[0], reverse=True)
        for i in range(n):
            pos = lst[i][0]
            sp = lst[i][1]
            time = (target - pos) / sp
            stack.append(time)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
