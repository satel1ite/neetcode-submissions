class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans = 0
        stack = []
        for i, h in enumerate(heights):
            cur_i = i
            if stack and h > stack[-1][1]:
                stack.append([i, h])
            else:
                while stack and h < stack[-1][1]:
                    cur_i, cur_h = stack.pop()
                    cur_area = (i-cur_i)*cur_h
                    ans = max(ans, cur_area)
                stack.append([cur_i, h])
        if stack:
            for cur_i, cur_h in stack:
                cur_area = (len(heights)-cur_i)*cur_h
                ans = max(ans, cur_area)
        return ans 