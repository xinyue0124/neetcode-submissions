class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # time is 1 unit time to process a single task
        # minimize the total time -> process the most freq one
        count = Counter(tasks) # char -> count
        maxHeap = [-c for c in count.values()]
        heapq.heapify(maxHeap)
        time = 0
        q = deque() # [-c, idletime]
        while maxHeap or q:
            time += 1
            if maxHeap:
                c = 1 + heapq.heappop(maxHeap)
                if c:
                    q.append([c, time + n])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time
