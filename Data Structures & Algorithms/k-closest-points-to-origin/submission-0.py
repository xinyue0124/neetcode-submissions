class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap = [(p[0]**2 + p[1]**2, p[0], p[1] )for p in points]
        heapq.heapify(minheap)
        res = []
        for _ in range(k):
            dist, x, y = heapq.heappop(minheap)
            res.append([x, y])
        return res
