class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        m = len(matrix)
        n = len(matrix[0])
        right = m*n - 1
        while left <= right:
            mid = (left + right) // 2
            r = mid // n
            c = mid % n
            mid_val = matrix[r][c]
            if mid_val == target:
                return True
            elif mid_val < target:
                left = mid + 1
            else:
                right = mid - 1
        return False