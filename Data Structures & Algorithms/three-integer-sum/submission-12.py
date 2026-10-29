class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        
        i = 0
        while i < len(nums) - 2:
            l = i + 1
            r = len(nums) - 1

            while l < r:
                if nums[i] + nums[l] + nums[r] < 0:
                    prev = nums[l]
                    while l < r and nums[l] == prev:
                        l += 1
                elif nums[i] + nums[l] + nums[r] > 0:
                    prev = nums[r]
                    while l < r and nums[r] == prev:
                        r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    prev = nums[l]
                    while l < r and nums[l] == prev:
                        l += 1
            prev = nums[i]
            while i < len(nums) - 1 and nums[i] == prev:
                i += 1
        
        return res
