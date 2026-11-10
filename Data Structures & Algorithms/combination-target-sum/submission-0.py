class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []

        def findCombinations(nums, target, curr_combination, curr_sum):
            if nums == []:
                return

            if curr_sum == target:
                res.append(curr_combination)
                return

            if curr_sum > target:
                return

            with_i = curr_combination.copy()
            with_i.append(nums[0])
            without_i = curr_combination.copy()

            findCombinations(nums, target, with_i, curr_sum + nums[0])
            findCombinations(nums[1:], target, without_i, curr_sum)

        findCombinations(nums, target, [], 0)
        return res

            
            
            


            

