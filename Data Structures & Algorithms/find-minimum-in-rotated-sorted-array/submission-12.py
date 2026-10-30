class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        m = (l + r) // 2
        res = nums[m]

        while l <= r:
            if nums[l] < nums[m] < nums[r]:
                return nums[l]

            res = min(res, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
            m = (l + r) // 2
        
        return res