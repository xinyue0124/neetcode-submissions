class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # max heap
        stones = [-s for s in stones]
        maxHeap = stones
        heapq.heapify(maxHeap)
        while len(maxHeap) > 1:
            stone1 = heapq.heappop(maxHeap)
            stone2 = heapq.heappop(maxHeap)
            if (stone1 - stone2) != 0:
                heapq.heappush(maxHeap,(stone1 - stone2))
        return -maxHeap[0] if maxHeap else 0
        
        