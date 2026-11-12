class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        prev = set()
        for n in nums:
            if n in prev:
                return True
            prev.add(n)
        return False