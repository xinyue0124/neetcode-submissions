class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # step 1: make all them negative in order to get the max
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            first = -heapq.heappop(stones)
            second = -heapq.heappop(stones)
            if first != second:
                diff = first - second
                heapq.heappush(stones, -diff)
        return -stones[0] if stones else 0