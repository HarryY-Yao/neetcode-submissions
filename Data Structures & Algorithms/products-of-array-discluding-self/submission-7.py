class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [0] * n
        suffix = [0] * n
        res = []

        prefix[0] = suffix[n - 1] = 1
        for i in range(1, len(nums)):
            prefix[i] = nums[i - 1] * prefix[i - 1]  

        for i in range(n - 2, -1, -1):
            suffix[i] = nums[i + 1] * suffix[i + 1]
        
        for i in range(len(nums)):
            res.append(prefix[i] * suffix[i])
        
        return res
