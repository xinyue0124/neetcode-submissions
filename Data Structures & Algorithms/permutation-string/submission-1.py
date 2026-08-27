class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counts1, counts2 = [0] * 26, [0] * 26
        if len(s1) > len(s2):
            return False
        for c in s1:
            counts1[ord(c)- ord('a')] += 1
        l = 0
        for r in range(len(s2)):
            counts2[ord(s2[r])- ord('a')] += 1
            if (r - l + 1) > len(s1):
                counts2[ord(s2[l])- ord('a')] -= 1
                l += 1
            if (r - l + 1) == len(s1):
                if counts2 == counts1:
                    return True
        return False
                