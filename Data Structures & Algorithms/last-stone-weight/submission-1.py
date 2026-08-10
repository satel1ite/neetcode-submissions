import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [i*(-1) for i in stones]
        heapq.heapify(heap)
        while len(heap) > 1:
            x = heapq.heappop(heap)
            y = heapq.heappop(heap)
            if x < y:
                heapq.heappush(heap, x-y)
            else:
                heapq.heappush(heap, y-x)
        if heap:
            return heap[0]*(-1)
        return 0