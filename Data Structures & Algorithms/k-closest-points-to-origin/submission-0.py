import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = [(((x1)**2 + (y1)**2)*(-1), [x1, y1]) for x1, y1 in points]
        heapq.heapify(heap)
        while len(heap) > k:
            heapq.heappop(heap)
        return [he[1] for he in heap] 