class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        m = (l + r) // 2

        while l <= r:
            if nums[m] == target:
                return m
            
            if nums[l] < nums[r]:
                if target > nums[m]:
                    l = m + 1
                else:
                    r = m - 1
            
            else:
                if nums[m] >= nums[l]:
                    if nums[l] > target or nums[m] < target:
                        l = m + 1
                    else:
                        r = m - 1
                else:
                    if nums[r] < target or target < nums[m]:
                        r = m - 1
                    else:
                        l = m + 1
            m = (l + r) // 2
            
        return -1