class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # maxHeap:two root node
        # compare == then pop
        # different then add the difference to stones
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if second > first:
                heapq.heappush(stones, first - second)
        return -stones[0] if stones else 0

