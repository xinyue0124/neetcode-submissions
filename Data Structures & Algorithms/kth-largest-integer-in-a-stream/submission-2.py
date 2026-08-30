class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        #construct a min heap
        self.minheap = nums
        heapq.heapify(self.minheap)
        self.k = k
        while len(self.minheap) > self.k:
            heapq.heappop(self.minheap)

    def add(self, val: int) -> int:
        # add to heap
        heapq.heappush(self.minheap,val)
        if len(self.minheap) > self.k:
            heapq.heappop(self.minheap)
        return self.minheap[0]
