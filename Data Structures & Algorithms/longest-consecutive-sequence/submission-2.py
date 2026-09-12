class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)

        firstElements = []

        for num in numSet:
            if num - 1 not in numSet:
                firstElements.append(num)

        lmax = 0
        for n in firstElements:
            l = 1
            m = n + 1
            while m in numSet:
                l += 1
                m += 1
            lmax = max(l, lmax)
        
        return lmax