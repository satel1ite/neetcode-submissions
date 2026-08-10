class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = dict()
        for task in tasks:
            if task in counter:
                counter[task] += 1
            else:
                counter[task] = 1
        heap = [count * (-1) for count in counter.values()]
        heapq.heapify(heap)
        q = deque()
        time = 0
        while heap or q:
            time += 1
            if heap:
                el = heapq.heappop(heap)
                el += 1
                if el != 0:
                    q.append([el, time + n])
            if q and q[0][1] == time:
                heapq.heappush(heap, q.popleft()[0])
        return time
