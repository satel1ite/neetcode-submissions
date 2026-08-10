import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = [num*(-1) for num in nums]
        heapq.heapify(heap)
        for _ in range(k-1):
            heapq.heappop(heap)
        return heap[0]*(-1)