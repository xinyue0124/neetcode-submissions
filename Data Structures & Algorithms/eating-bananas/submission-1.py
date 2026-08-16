class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # k must between 1 and max(piles)
        # use binary search find the val
        l, r = 1, max(piles)
        res = r
        
        while l <= r:
            total = 0
            k = (l + r) // 2
            for p in piles:
                total += math.ceil(float(p)/ k)
            if total <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
        return res