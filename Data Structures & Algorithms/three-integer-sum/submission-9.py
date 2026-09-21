class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        out = []
        nums.sort()

        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1

            while (j < k):
                summed = nums[i] + nums[j] + nums[k]
                if summed > 0:
                    k -= 1
                elif summed < 0:
                    j += 1
                else:
                    output = [nums[i], nums[j], nums[k]]
                    if output not in res:
                        res.append(output)
                    j += 1
        return res    