class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lst = []
        for row in matrix:
            for a in row:
                lst.append(a)
        left = 0
        # m = len(matrix)
        # n = len(matrix[0])
        right = len(lst) - 1
        while left <= right:
            mid = (left + right) // 2
            if lst[mid] == target:
                return True
            elif lst[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False