class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # if (nums -1) not in nums it can be the start of longest
        # if nums + 1 exist in nums update longest until not exist
        
        numSet = set(nums)
        res = 0
        for n in numSet:
            if (n - 1) not in numSet:
                length = 0
                while (n + length) in numSet:
                    length += 1
                res = max(length, res)
        return res
