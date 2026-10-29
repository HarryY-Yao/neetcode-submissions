class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [0] * len(nums)
        suffix = [0] * len(nums)
        res = []
        count_pre = count_post = 1


        for i in range(len(nums)):
            prefix[i] = count_pre
            count_pre *= nums[i]
            
            suffix[len(nums) - 1 - i] = count_post
            count_post *= nums[len(nums) - 1 - i]

        for i in range(len(nums)):
            res.append(prefix[i] * suffix[i])
        
        return res
