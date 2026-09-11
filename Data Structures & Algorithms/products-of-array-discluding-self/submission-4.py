class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixes = []
        suffixes = []
        
        curr = 1
        for i in range(len(nums)):
            prefixes.append(curr)
            curr *= nums[i]
        
        curr = 1
        for i in range(len(nums) - 1, -1, -1):
            suffixes.append(curr)
            curr *= nums[i]
        suffixes.reverse()

        res = []
        for i in range(len(nums)):
            res.append(prefixes[i] * suffixes[i])


        return res